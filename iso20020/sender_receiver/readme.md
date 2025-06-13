
Transition from iso15022 to iso20022

https://www.iso20022.org/15022/uhb/mt516-25-field-72.htm

sender receiver Line 1    (code)(narrative)

sender receiver Line 2-6  (continuation of additional information) or (code)(narrative)

For iso20022 

Parse sender and receiver infomation 

    (code)(narrative + continuation of additional information)

Validate parse sender and receiver infomation 

    (code)(narrative + continuation of additional information) ensure does not exceed 140 char

🧾 Background Summary
ISO 15022 (MT Format):

Line 1: Starts with a code (e.g., /ACC/, /BNF/, /INS/) followed by narrative.

Line 2–6: May contain continuation of the narrative or additional code+narrative pairs.

ISO 20022 (XML-based):

Consolidates information into structured elements with clear tags like <Pty>, <Id>, <Nm>, <PstlAdr>, etc.

The goal is to preserve the meaning while flattening multi-line input and ensuring field length limits, e.g., max 140 characters.


✅ Goal
Parse:

Join sender/receiver lines into a single string per block.

Preserve the original code (e.g., /BNF/) and concatenate the narrative and continuation lines.

Validate:

Ensure that each final string does not exceed 140 characters.
