
Transition from iso15022 to iso20022

https://www.iso20022.org/15022/uhb/mt516-25-field-72.htm

sender receiver Line 1    (code)(narrative)

sender receiver Line 2-6  (continuation of additional information) or (code)(narrative)

For iso20022 

Parse sender and receiver infomation 

    (code)(narrative + continuation of additional information)

Validate parse sender and receiver infomation 

    (code)(narrative + continuation of additional information) ensure does not exceed 140 char
