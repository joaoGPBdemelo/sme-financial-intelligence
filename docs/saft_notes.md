# Notas SAF-T PT 1.04_01 (faturação)

_Rascunho gerado a partir de `schemas/SAFTPT1.04_01.xsd`. Preencha a coluna "Valor no gerador" e as regras de coerência._

## Header

| Campo | Obrig. | Repete | Tipo / regras | Valor no gerador |
|---|---|---|---|---|
| `AuditFileVersion` | sim |  | string · pattern=1\.04_01 | |
| `CompanyID` | sim |  | string · pattern=([0-9]{9})+|([^^]+ [0-9/]+) · minLength=1 · maxLength=50 | |
| `TaxRegistrationNumber` | sim |  | integer · minInclusive=100000000 · maxInclusive=999999999 | |
| `TaxAccountingBasis` | sim |  | string · valores: C, E, F, I, P, R, S, T | |
| `CompanyName` | sim |  | string · minLength=1 · maxLength=100 | |
| `BusinessName` | não |  | string · minLength=1 · maxLength=60 | |
| `CompanyAddress/BuildingNumber` | não |  | string · minLength=1 · maxLength=10 | |
| `CompanyAddress/StreetName` | não |  | string · minLength=1 · maxLength=200 | |
| `CompanyAddress/AddressDetail` | sim |  | string · minLength=1 · maxLength=210 | |
| `CompanyAddress/City` | sim |  | string · minLength=1 · maxLength=50 | |
| `CompanyAddress/PostalCode` | sim |  | string · minLength=1 · maxLength=20 | |
| `CompanyAddress/Region` | não |  | string · minLength=1 · maxLength=50 | |
| `CompanyAddress/Country` | sim |  | string · pattern=AD|AE|AF|AG|AI|AL|AM|AO|AQ|AR|AS|AT|AU|AW|AX|AZ|BA|BB|BD|BE|BF|BG|BH|BI|BJ|BL|BM|BN|BO|BQ|BR|BS|BT|BV|BW|BY|BZ|CA|CC|CD|CF|CG|CH|CI|CK|CL|CM|CN|CO|CR|CU|CV|CW|CX|CY|CZ|DE|DJ|DK|DM|DO|DZ|EC|EE|EG|EH|ER|ES|ET|FI|FJ|FK|FM|FO|FR|GA|GB|GD|GE|GF|GG|GH|GI|GL|GM|GN|GP|GQ|GR|GS|GT|GU|GW|GY|HK|HM|HN|HR|HT|HU|ID|IE|IL|IM|IN|IO|IQ|IR|IS|IT|JE|JM|JO|JP|KE|KG|KH|KI|KM|KN|KP|KR|KW|KY|KZ|LA|LB|LC|LI|LK|LR|LS|LT|LU|LV|LY|MA|MC|MD|ME|MF|MG|MH|MK|ML|MM|MN|MO|MP|MQ|MR|MS|MT|MU|MV|MW|MX|MY|MZ|NA|NC|NE|NF|NG|NI|NL|NO|NP|NR|NU|NZ|OM|PA|PE|PF|PG|PH|PK|PL|PM|PN|PR|PS|PT|PW|PY|QA|RE|RO|RS|RU|RW|SA|SB|SC|SD|SE|SG|SH|SI|SJ|SK|SL|SM|SN|SO|SR|SS|ST|SV|SX|SY|SZ|TC|TD|TF|TG|TH|TJ|TK|TL|TM|TN|TO|TR|TT|TV|TW|TZ|UA|UG|UM|US|UY|UZ|VA|VC|VE|VG|VI|VN|VU|WF|WS|XK|YE|YT|ZA|ZM|ZW | |
| `FiscalYear` | sim |  | integer · minInclusive=2000 · maxInclusive=9999 | |
| `StartDate` | sim |  | date · minInclusive=2000-01-01 · maxInclusive=9999-12-31 | |
| `EndDate` | sim |  | date · minInclusive=2000-01-01 · maxInclusive=9999-12-31 | |
| `CurrencyCode` | sim |  | string · valores: EUR | |
| `DateCreated` | sim |  | date · minInclusive=2000-01-01 · maxInclusive=9999-12-31 | |
| `TaxEntity` | sim |  | string · minLength=1 · maxLength=20 | |
| `ProductCompanyTaxID` | sim |  | string · minLength=1 · maxLength=30 | |
| `SoftwareCertificateNumber` | sim |  | nonNegativeInteger | |
| `ProductID` | sim |  | string · pattern=[^/]+/[^/]+ · minLength=3 · maxLength=255 | |
| `ProductVersion` | sim |  | string · minLength=1 · maxLength=30 | |
| `HeaderComment` | não |  | string · minLength=1 · maxLength=255 | |
| `Telephone` | não |  | string · minLength=1 · maxLength=20 | |
| `Fax` | não |  | string · minLength=1 · maxLength=20 | |
| `Email` | não |  | string · minLength=1 · maxLength=254 | |
| `Website` | não |  | string · minLength=1 · maxLength=60 | |

## Customer

| Campo | Obrig. | Repete | Tipo / regras | Valor no gerador |
|---|---|---|---|---|
| `CustomerID` | sim |  | string · minLength=1 · maxLength=30 | |
| `AccountID` | sim |  | string · pattern=(([^^]*)|Desconhecido) · minLength=1 · maxLength=30 | |
| `CustomerTaxID` | sim |  | string · minLength=1 · maxLength=30 | |
| `CompanyName` | sim |  | string · minLength=1 · maxLength=100 | |
| `Contact` | não |  | string · minLength=1 · maxLength=50 | |
| `BillingAddress/BuildingNumber` | não |  | string · minLength=1 · maxLength=10 | |
| `BillingAddress/StreetName` | não |  | string · minLength=1 · maxLength=200 | |
| `BillingAddress/AddressDetail` | sim |  | string · minLength=1 · maxLength=210 | |
| `BillingAddress/City` | sim |  | string · minLength=1 · maxLength=50 | |
| `BillingAddress/PostalCode` | sim |  | string · minLength=1 · maxLength=20 | |
| `BillingAddress/Region` | não |  | string · minLength=1 · maxLength=50 | |
| `BillingAddress/Country` | sim |  | string · pattern=AD|AE|AF|AG|AI|AL|AM|AO|AQ|AR|AS|AT|AU|AW|AX|AZ|BA|BB|BD|BE|BF|BG|BH|BI|BJ|BL|BM|BN|BO|BQ|BR|BS|BT|BV|BW|BY|BZ|CA|CC|CD|CF|CG|CH|CI|CK|CL|CM|CN|CO|CR|CU|CV|CW|CX|CY|CZ|DE|DJ|DK|DM|DO|DZ|EC|EE|EG|EH|ER|ES|ET|FI|FJ|FK|FM|FO|FR|GA|GB|GD|GE|GF|GG|GH|GI|GL|GM|GN|GP|GQ|GR|GS|GT|GU|GW|GY|HK|HM|HN|HR|HT|HU|ID|IE|IL|IM|IN|IO|IQ|IR|IS|IT|JE|JM|JO|JP|KE|KG|KH|KI|KM|KN|KP|KR|KW|KY|KZ|LA|LB|LC|LI|LK|LR|LS|LT|LU|LV|LY|MA|MC|MD|ME|MF|MG|MH|MK|ML|MM|MN|MO|MP|MQ|MR|MS|MT|MU|MV|MW|MX|MY|MZ|NA|NC|NE|NF|NG|NI|NL|NO|NP|NR|NU|NZ|OM|PA|PE|PF|PG|PH|PK|PL|PM|PN|PR|PS|PT|PW|PY|QA|RE|RO|RS|RU|RW|SA|SB|SC|SD|SE|SG|SH|SI|SJ|SK|SL|SM|SN|SO|SR|SS|ST|SV|SX|SY|SZ|TC|TD|TF|TG|TH|TJ|TK|TL|TM|TN|TO|TR|TT|TV|TW|TZ|UA|UG|UM|US|UY|UZ|VA|VC|VE|VG|VI|VN|VU|WF|WS|XK|YE|YT|ZA|ZM|ZW|Desconhecido | |
| `ShipToAddress[]/BuildingNumber` | não |  | string · minLength=1 · maxLength=10 | |
| `ShipToAddress[]/StreetName` | não |  | string · minLength=1 · maxLength=200 | |
| `ShipToAddress[]/AddressDetail` | sim |  | string · minLength=1 · maxLength=210 | |
| `ShipToAddress[]/City` | sim |  | string · minLength=1 · maxLength=50 | |
| `ShipToAddress[]/PostalCode` | sim |  | string · minLength=1 · maxLength=20 | |
| `ShipToAddress[]/Region` | não |  | string · minLength=1 · maxLength=50 | |
| `ShipToAddress[]/Country` | sim |  | string · pattern=AD|AE|AF|AG|AI|AL|AM|AO|AQ|AR|AS|AT|AU|AW|AX|AZ|BA|BB|BD|BE|BF|BG|BH|BI|BJ|BL|BM|BN|BO|BQ|BR|BS|BT|BV|BW|BY|BZ|CA|CC|CD|CF|CG|CH|CI|CK|CL|CM|CN|CO|CR|CU|CV|CW|CX|CY|CZ|DE|DJ|DK|DM|DO|DZ|EC|EE|EG|EH|ER|ES|ET|FI|FJ|FK|FM|FO|FR|GA|GB|GD|GE|GF|GG|GH|GI|GL|GM|GN|GP|GQ|GR|GS|GT|GU|GW|GY|HK|HM|HN|HR|HT|HU|ID|IE|IL|IM|IN|IO|IQ|IR|IS|IT|JE|JM|JO|JP|KE|KG|KH|KI|KM|KN|KP|KR|KW|KY|KZ|LA|LB|LC|LI|LK|LR|LS|LT|LU|LV|LY|MA|MC|MD|ME|MF|MG|MH|MK|ML|MM|MN|MO|MP|MQ|MR|MS|MT|MU|MV|MW|MX|MY|MZ|NA|NC|NE|NF|NG|NI|NL|NO|NP|NR|NU|NZ|OM|PA|PE|PF|PG|PH|PK|PL|PM|PN|PR|PS|PT|PW|PY|QA|RE|RO|RS|RU|RW|SA|SB|SC|SD|SE|SG|SH|SI|SJ|SK|SL|SM|SN|SO|SR|SS|ST|SV|SX|SY|SZ|TC|TD|TF|TG|TH|TJ|TK|TL|TM|TN|TO|TR|TT|TV|TW|TZ|UA|UG|UM|US|UY|UZ|VA|VC|VE|VG|VI|VN|VU|WF|WS|XK|YE|YT|ZA|ZM|ZW|Desconhecido | |
| `Telephone` | não |  | string · minLength=1 · maxLength=20 | |
| `Fax` | não |  | string · minLength=1 · maxLength=20 | |
| `Email` | não |  | string · minLength=1 · maxLength=254 | |
| `Website` | não |  | string · minLength=1 · maxLength=60 | |
| `SelfBillingIndicator` | sim |  | integer · minInclusive=0 · maxInclusive=1 | |

## Invoice (bloco opcional, pode repetir)

| Campo | Obrig. | Repete | Tipo / regras | Valor no gerador |
|---|---|---|---|---|
| `InvoiceNo` | sim |  | string · pattern=[^ ]+ [^/^ ]+/[0-9]+ · minLength=1 · maxLength=60 | |
| `ATCUD` | sim |  | string · minLength=1 · maxLength=100 | |
| `DocumentStatus/InvoiceStatus` | sim |  | string · valores: N, S, A, R, F | |
| `DocumentStatus/InvoiceStatusDate` | sim |  | dateTime | |
| `DocumentStatus/Reason` | não |  | string · minLength=1 · maxLength=50 | |
| `DocumentStatus/SourceID` | sim |  | string · minLength=1 · maxLength=30 | |
| `DocumentStatus/SourceBilling` | sim |  | string · valores: P, I, M | |
| `Hash` | sim |  | string · minLength=1 · maxLength=172 | |
| `HashControl` | sim |  | string · pattern=[0-9]+|[0-9]+[\.][0-9]+|[0-9]+-[A-Z]{2}(M )([^/^ ]+[/][0-9]+)|[0-9]+-[A-Z]{2}(D )([^ ]+ [^/^ ]+[/][0-9]+) · minLength=1 · maxLength=70 | |
| `Period` | não |  | integer · minInclusive=1 · maxInclusive=12 | |
| `InvoiceDate` | sim |  | date | |
| `InvoiceType` | sim |  | string · valores: FT, FS, FR, ND, NC, VD, TV, TD, AA, DA, RP, RE … | |
| `SpecialRegimes/SelfBillingIndicator` | sim |  | integer · minInclusive=0 · maxInclusive=1 | |
| `SpecialRegimes/CashVATSchemeIndicator` | sim |  | integer · minInclusive=0 · maxInclusive=1 | |
| `SpecialRegimes/ThirdPartiesBillingIndicator` | sim |  | integer · minInclusive=0 · maxInclusive=1 | |
| `SourceID` | sim |  | string · minLength=1 · maxLength=30 | |
| `EACCode` | não |  | string · pattern=(([0-9]*)) · length=5 | |
| `SystemEntryDate` | sim |  | dateTime | |
| `TransactionID` | não |  | string · pattern=[1-9][0-9]{3}-[01][0-9]-[0-3][0-9] [^ ]{1,30} [^ ]{1,20} · minLength=1 · maxLength=70 | |
| `CustomerID` | sim |  | string · minLength=1 · maxLength=30 | |
| `ShipTo/DeliveryID` | não | sim | string · minLength=1 · maxLength=255 | |
| `ShipTo/DeliveryDate` | não |  | date | |
| `ShipTo/WarehouseID` | não |  | string · minLength=1 · maxLength=50 | |
| `ShipTo/LocationID` | não |  | string · minLength=1 · maxLength=30 | |
| `ShipTo/Address/BuildingNumber` | não |  | string · minLength=1 · maxLength=10 | |
| `ShipTo/Address/StreetName` | não |  | string · minLength=1 · maxLength=200 | |
| `ShipTo/Address/AddressDetail` | sim |  | string · minLength=1 · maxLength=210 | |
| `ShipTo/Address/City` | sim |  | string · minLength=1 · maxLength=50 | |
| `ShipTo/Address/PostalCode` | sim |  | string · minLength=1 · maxLength=20 | |
| `ShipTo/Address/Region` | não |  | string · minLength=1 · maxLength=50 | |
| `ShipTo/Address/Country` | sim |  | string · pattern=AD|AE|AF|AG|AI|AL|AM|AO|AQ|AR|AS|AT|AU|AW|AX|AZ|BA|BB|BD|BE|BF|BG|BH|BI|BJ|BL|BM|BN|BO|BQ|BR|BS|BT|BV|BW|BY|BZ|CA|CC|CD|CF|CG|CH|CI|CK|CL|CM|CN|CO|CR|CU|CV|CW|CX|CY|CZ|DE|DJ|DK|DM|DO|DZ|EC|EE|EG|EH|ER|ES|ET|FI|FJ|FK|FM|FO|FR|GA|GB|GD|GE|GF|GG|GH|GI|GL|GM|GN|GP|GQ|GR|GS|GT|GU|GW|GY|HK|HM|HN|HR|HT|HU|ID|IE|IL|IM|IN|IO|IQ|IR|IS|IT|JE|JM|JO|JP|KE|KG|KH|KI|KM|KN|KP|KR|KW|KY|KZ|LA|LB|LC|LI|LK|LR|LS|LT|LU|LV|LY|MA|MC|MD|ME|MF|MG|MH|MK|ML|MM|MN|MO|MP|MQ|MR|MS|MT|MU|MV|MW|MX|MY|MZ|NA|NC|NE|NF|NG|NI|NL|NO|NP|NR|NU|NZ|OM|PA|PE|PF|PG|PH|PK|PL|PM|PN|PR|PS|PT|PW|PY|QA|RE|RO|RS|RU|RW|SA|SB|SC|SD|SE|SG|SH|SI|SJ|SK|SL|SM|SN|SO|SR|SS|ST|SV|SX|SY|SZ|TC|TD|TF|TG|TH|TJ|TK|TL|TM|TN|TO|TR|TT|TV|TW|TZ|UA|UG|UM|US|UY|UZ|VA|VC|VE|VG|VI|VN|VU|WF|WS|XK|YE|YT|ZA|ZM|ZW|Desconhecido | |
| `ShipFrom/DeliveryID` | não | sim | string · minLength=1 · maxLength=255 | |
| `ShipFrom/DeliveryDate` | não |  | date | |
| `ShipFrom/WarehouseID` | não |  | string · minLength=1 · maxLength=50 | |
| `ShipFrom/LocationID` | não |  | string · minLength=1 · maxLength=30 | |
| `ShipFrom/Address/BuildingNumber` | não |  | string · minLength=1 · maxLength=10 | |
| `ShipFrom/Address/StreetName` | não |  | string · minLength=1 · maxLength=200 | |
| `ShipFrom/Address/AddressDetail` | sim |  | string · minLength=1 · maxLength=210 | |
| `ShipFrom/Address/City` | sim |  | string · minLength=1 · maxLength=50 | |
| `ShipFrom/Address/PostalCode` | sim |  | string · minLength=1 · maxLength=20 | |
| `ShipFrom/Address/Region` | não |  | string · minLength=1 · maxLength=50 | |
| `ShipFrom/Address/Country` | sim |  | string · pattern=AD|AE|AF|AG|AI|AL|AM|AO|AQ|AR|AS|AT|AU|AW|AX|AZ|BA|BB|BD|BE|BF|BG|BH|BI|BJ|BL|BM|BN|BO|BQ|BR|BS|BT|BV|BW|BY|BZ|CA|CC|CD|CF|CG|CH|CI|CK|CL|CM|CN|CO|CR|CU|CV|CW|CX|CY|CZ|DE|DJ|DK|DM|DO|DZ|EC|EE|EG|EH|ER|ES|ET|FI|FJ|FK|FM|FO|FR|GA|GB|GD|GE|GF|GG|GH|GI|GL|GM|GN|GP|GQ|GR|GS|GT|GU|GW|GY|HK|HM|HN|HR|HT|HU|ID|IE|IL|IM|IN|IO|IQ|IR|IS|IT|JE|JM|JO|JP|KE|KG|KH|KI|KM|KN|KP|KR|KW|KY|KZ|LA|LB|LC|LI|LK|LR|LS|LT|LU|LV|LY|MA|MC|MD|ME|MF|MG|MH|MK|ML|MM|MN|MO|MP|MQ|MR|MS|MT|MU|MV|MW|MX|MY|MZ|NA|NC|NE|NF|NG|NI|NL|NO|NP|NR|NU|NZ|OM|PA|PE|PF|PG|PH|PK|PL|PM|PN|PR|PS|PT|PW|PY|QA|RE|RO|RS|RU|RW|SA|SB|SC|SD|SE|SG|SH|SI|SJ|SK|SL|SM|SN|SO|SR|SS|ST|SV|SX|SY|SZ|TC|TD|TF|TG|TH|TJ|TK|TL|TM|TN|TO|TR|TT|TV|TW|TZ|UA|UG|UM|US|UY|UZ|VA|VC|VE|VG|VI|VN|VU|WF|WS|XK|YE|YT|ZA|ZM|ZW|Desconhecido | |
| `MovementEndTime` | não |  | dateTime | |
| `MovementStartTime` | não |  | dateTime | |
| `Line[]/LineNumber` | sim |  | nonNegativeInteger | |
| `Line[]/OrderReferences[]/OriginatingON` | não |  | string · minLength=1 · maxLength=60 | |
| `Line[]/OrderReferences[]/OrderDate` | não |  | date | |
| `Line[]/ProductCode` | sim |  | string · minLength=1 · maxLength=60 | |
| `Line[]/ProductDescription` | sim |  | string · minLength=2 · maxLength=200 | |
| `Line[]/Quantity` | sim |  | decimal · minInclusive=0.00 | |
| `Line[]/UnitOfMeasure` | sim |  | string · minLength=1 · maxLength=20 | |
| `Line[]/UnitPrice` | sim |  | decimal · minInclusive=0.00 | |
| `Line[]/TaxBase` | não |  | decimal · minInclusive=0.00 | |
| `Line[]/TaxPointDate` | sim |  | date | |
| `Line[]/References[]/Reference` | não |  | string · minLength=1 · maxLength=60 | |
| `Line[]/References[]/Reason` | não |  | string · minLength=1 · maxLength=50 | |
| `Line[]/Description` | sim |  | string · minLength=1 · maxLength=200 | |
| `Line[]/ProductSerialNumber/SerialNumber` | sim | sim | string · minLength=1 · maxLength=100 | |
| `Line[]/DebitAmount` | escolha |  | decimal · minInclusive=0.00 | |
| `Line[]/CreditAmount` | escolha |  | decimal · minInclusive=0.00 | |
| `Line[]/Tax/TaxType` | sim |  | string · valores: IVA, IS, NS | |
| `Line[]/Tax/TaxCountryRegion` | sim |  | string · pattern=AD|AE|AF|AG|AI|AL|AM|AO|AQ|AR|AS|AT|AU|AW|AX|AZ|BA|BB|BD|BE|BF|BG|BH|BI|BJ|BL|BM|BN|BO|BQ|BR|BS|BT|BV|BW|BY|BZ|CA|CC|CD|CF|CG|CH|CI|CK|CL|CM|CN|CO|CR|CU|CV|CW|CX|CY|CZ|DE|DJ|DK|DM|DO|DZ|EC|EE|EG|EH|ER|ES|ET|FI|FJ|FK|FM|FO|FR|GA|GB|GD|GE|GF|GG|GH|GI|GL|GM|GN|GP|GQ|GR|GS|GT|GU|GW|GY|HK|HM|HN|HR|HT|HU|ID|IE|IL|IM|IN|IO|IQ|IR|IS|IT|JE|JM|JO|JP|KE|KG|KH|KI|KM|KN|KP|KR|KW|KY|KZ|LA|LB|LC|LI|LK|LR|LS|LT|LU|LV|LY|MA|MC|MD|ME|MF|MG|MH|MK|ML|MM|MN|MO|MP|MQ|MR|MS|MT|MU|MV|MW|MX|MY|MZ|NA|NC|NE|NF|NG|NI|NL|NO|NP|NR|NU|NZ|OM|PA|PE|PF|PG|PH|PK|PL|PM|PN|PR|PS|PT|PW|PY|QA|RE|RO|RS|RU|RW|SA|SB|SC|SD|SE|SG|SH|SI|SJ|SK|SL|SM|SN|SO|SR|SS|ST|SV|SX|SY|SZ|TC|TD|TF|TG|TH|TJ|TK|TL|TM|TN|TO|TR|TT|TV|TW|TZ|UA|UG|UM|US|UY|UZ|VA|VC|VE|VG|VI|VN|VU|WF|WS|XK|YE|YT|ZA|ZM|ZW|PT-AC|PT-MA | |
| `Line[]/Tax/TaxCode` | sim |  | string · minLength=1 · maxLength=10 · pattern=RED|INT|NOR|ISE|OUT|([a-zA-Z0-9\.])*|NS | |
| `Line[]/Tax/TaxPercentage` | escolha |  | decimal · minInclusive=0.00 | |
| `Line[]/Tax/TaxAmount` | escolha |  | decimal · minInclusive=0.00 | |
| `Line[]/TaxExemptionReason` | não |  | string · minLength=6 · maxLength=60 | |
| `Line[]/TaxExemptionCode` | não |  | string · pattern=(M[0-9]{2})+ | |
| `Line[]/SettlementAmount` | não |  | decimal · minInclusive=0.00 | |
| `Line[]/CustomsInformation/ARCNo` | não | sim | string · minLength=1 · maxLength=21 | |
| `Line[]/CustomsInformation/IECAmount` | não |  | decimal · minInclusive=0.00 | |
| `DocumentTotals/TaxPayable` | sim |  | decimal · minInclusive=0.00 | |
| `DocumentTotals/NetTotal` | sim |  | decimal · minInclusive=0.00 | |
| `DocumentTotals/GrossTotal` | sim |  | decimal · minInclusive=0.00 | |
| `DocumentTotals/Currency/CurrencyCode` | sim |  | string · pattern=AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BOV|BRL|BSD|BTN|BWP|BYN|BYR|BZD|CAD|CDF|CHE|CHF|CHW|CLF|CLP|CNY|COP|COU|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|FJD|FKP|GBP|GEL|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|INR|IQD|IRR|ISK|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LTL|LVL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MRU|MUR|MVR|MWK|MXN|MXV|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLE|SLL|SOS|SRD|SSP|STD|STN|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TWD|TZS|UAH|UGX|USD|USN|USS|UYI|UYU|UZS|VED|VEF|VES|VND|VUV|WST|XAF|XAG|XAU|XBA|XBB|XBC|XBD|XCD|XDR|XFU|XOF|XPD|XPF|XPT|XSU|XUA|YER|ZAR|ZMW|ZWL|EEK|SKK|TMM|ZMK|ZWD|ZWR | |
| `DocumentTotals/Currency/CurrencyAmount` | sim |  | decimal · minInclusive=0.00 | |
| `DocumentTotals/Currency/ExchangeRate` | sim |  | decimal · minInclusive=0.00 | |
| `DocumentTotals/Settlement[]/SettlementDiscount` | não |  | string · minLength=1 · maxLength=30 | |
| `DocumentTotals/Settlement[]/SettlementAmount` | não |  | decimal · minInclusive=0.00 | |
| `DocumentTotals/Settlement[]/SettlementDate` | não |  | date | |
| `DocumentTotals/Settlement[]/PaymentTerms` | não |  | string · minLength=1 · maxLength=100 | |
| `DocumentTotals/Payment[]/PaymentMechanism` | não |  | string · valores: CC, CD, CH, CI, CO, CS, DE, LC, MB, NU, OU, PR … | |
| `DocumentTotals/Payment[]/PaymentAmount` | sim |  | decimal · minInclusive=0.00 | |
| `DocumentTotals/Payment[]/PaymentDate` | sim |  | date | |
| `WithholdingTax[]/WithholdingTaxType` | não |  | string · valores: IRS, IRC, IS | |
| `WithholdingTax[]/WithholdingTaxDescription` | não |  | string · minLength=1 · maxLength=60 | |
| `WithholdingTax[]/WithholdingTaxAmount` | sim |  | decimal · minInclusive=0.00 | |

## Regras de coerência

- O `CustomerID` de cada fatura existe nos MasterFiles
- GrossTotal = NetTotal + IVA
- Cada Payment referencia faturas que existem
- (acrescente as suas)
