"""Gera um rascunho de notas (Markdown) com os campos de blocos do SAF-T a partir do XSD.

Uso:
    python scripts/xsd_to_notes.py [caminho_do_xsd] [ficheiro_md] [blocos...]

Exemplo:
    python scripts/xsd_to_notes.py schemas/SAFTPT1.04_01.xsd docs/saft_notes.md

Se não indicar blocos, usa: Header Customer Product TaxTableEntry Invoice Payment

Para cada bloco sai uma tabela com:
    Campo        caminho relativo ao bloco (ex.: DocumentTotals/NetTotal)
    Obrig.       sim / não / escolha (um de vários alternativos)
    Repete       sim, se o campo pode aparecer várias vezes
    Tipo/regras  tipo, tamanho máximo, valores permitidos...
    Valor no gerador   fica em branco: é a sua decisão

"Obrig. = sim" significa obrigatório DENTRO do bloco pai. Se o próprio bloco
for opcional, a coluna do bloco (cabeçalho) avisa.
"""

import sys
import xml.etree.ElementTree as ET
from pathlib import Path

XS = "{http://www.w3.org/2001/XMLSchema}"
DEFAULT_BLOCKS = ["Header", "Customer", "Product", "TaxTableEntry", "Invoice", "Payment"]


def local(name):
    return (name or "").split(":")[-1]


class Schema:
    def __init__(self, path):
        root = ET.parse(path).getroot()
        self.elements = {e.get("name"): e for e in root.findall(f"{XS}element")}
        self.ctypes = {t.get("name"): t for t in root.findall(f"{XS}complexType")}
        self.stypes = {t.get("name"): t for t in root.findall(f"{XS}simpleType")}

    def find(self, target):
        if target in self.elements:
            return self.elements[target]
        for definition in list(self.elements.values()) + list(self.ctypes.values()):
            for el in definition.iter(f"{XS}element"):
                if el.get("name") == target:
                    return el
        return None

    def children(self, node, in_choice=False):
        """Filhos diretos, atravessando sequence/choice/extension. Devolve (elemento, em_escolha)."""
        for child in node:
            tag = child.tag.replace(XS, "")
            if tag == "element":
                yield child, in_choice
            elif tag == "choice":
                yield from self.children(child, True)
            elif tag in ("sequence", "all", "complexContent", "simpleContent"):
                yield from self.children(child, in_choice)
            elif tag == "extension":
                base = self.ctypes.get(local(child.get("base")))
                if base is not None:
                    yield from self.children(base, in_choice)
                yield from self.children(child, in_choice)

    def rules(self, simple_type, depth=0):
        if simple_type is None or depth > 5:
            return []
        restriction = simple_type.find(f"{XS}restriction")
        if restriction is None:
            return []
        base = local(restriction.get("base"))
        out = self.rules(self.stypes.get(base), depth + 1) if base in self.stypes else [base]
        enums = []
        for facet in restriction:
            tag = facet.tag.replace(XS, "")
            value = facet.get("value")
            if tag == "enumeration":
                enums.append(value)
            elif tag != "annotation" and value is not None:
                out.append(f"{tag}={value}")
        if enums:
            out.append("valores: " + ", ".join(enums[:12]) + (" …" if len(enums) > 12 else ""))
        return out

    def flatten(self, el, prefix="", in_choice=False, seen=frozenset()):
        """Percorre o bloco e devolve linhas (caminho, obrig, repete, tipo/regras) só das folhas."""
        node = self.elements.get(local(el.get("ref")), el) if el.get("ref") else el
        name = node.get("name") or "?"
        path = f"{prefix}{name}"
        lo, hi = el.get("minOccurs", "1"), el.get("maxOccurs", "1")
        required = "escolha" if in_choice else ("não" if lo == "0" else "sim")
        repeats = "sim" if hi == "unbounded" or (hi.isdigit() and int(hi) > 1) else ""

        type_name = local(node.get("type"))
        inline = node.find(f"{XS}complexType")
        definition = inline if inline is not None else self.ctypes.get(type_name)

        if definition is not None and name not in seen:
            kids = list(self.children(definition))
            if kids:
                rows = []
                # um pai repetível aparece no caminho como Nome[] (ex.: Line[]/Quantity)
                group = path + ("[]" if repeats else "")
                for child, choice in kids:
                    rows += self.flatten(child, group + "/", choice, seen | {name})
                return rows
        simple = node.find(f"{XS}simpleType")
        if simple is None:
            simple = self.stypes.get(type_name)
        info = " · ".join(self.rules(simple)) or type_name
        return [(path, required, repeats, info, lo, hi)]


def table(schema, block):
    el = schema.find(block)
    if el is None:
        return f"## {block}\n\n_Elemento não encontrado no XSD._\n"
    lo, hi = el.get("minOccurs", "1"), el.get("maxOccurs", "1")
    notes = []
    if lo == "0":
        notes.append("bloco opcional")
    if hi == "unbounded" or (hi.isdigit() and int(hi) > 1):
        notes.append("pode repetir")
    head = f"## {block}" + (f" ({', '.join(notes)})" if notes else "")

    lines = [
        head,
        "",
        "| Campo | Obrig. | Repete | Tipo / regras | Valor no gerador |",
        "|---|---|---|---|---|",
    ]
    rows = schema.flatten(el)
    # remove o nome do próprio bloco do início do caminho
    for path, req, rep, info, _lo, _hi in rows:
        short = path.split("/", 1)[1] if "/" in path else path
        lines.append(f"| `{short}` | {req} | {rep} | {info} | |")
    lines.append("")
    return "\n".join(lines)


def main():
    xsd = sys.argv[1] if len(sys.argv) > 1 else "schemas/SAFTPT1.04_01.xsd"
    out = sys.argv[2] if len(sys.argv) > 2 else "docs/saft_notes.md"
    blocks = sys.argv[3:] or DEFAULT_BLOCKS

    schema = Schema(xsd)
    parts = [
        "# Notas SAF-T PT 1.04_01 (faturação)",
        "",
        f'_Rascunho gerado a partir de `{xsd}`. Preencha a coluna "Valor no gerador" e as regras de coerência._',
        "",
    ]
    parts += [table(schema, b) for b in blocks]
    parts += [
        "## Regras de coerência",
        "",
        "- O `CustomerID` de cada fatura existe nos MasterFiles",
        "- GrossTotal = NetTotal + IVA",
        "- Cada Payment referencia faturas que existem",
        "- (acrescente as suas)",
        "",
    ]

    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text("\n".join(parts), encoding="utf-8")
    print(f"Notas geradas: {out} ({len(blocks)} blocos)")


if __name__ == "__main__":
    main()
