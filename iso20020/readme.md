In ISO 20022 (especially when dealing with SWIFT-like MT/MX messages that are free-form or semi-structured), fields like /ACC/, /INS/, and /BNF/ represent parts of Sender to Receiver Information (SRI) — additional instructions passed along the payment chain.

Problem:
You want to parse a list of such lines, and when a line starts with a tag like /ACC/, /INS/, or /BNF/, treat it as a new field. If it doesn't, join it to the previous line.
