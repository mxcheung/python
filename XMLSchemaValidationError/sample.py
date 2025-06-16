
import xmlschema
from xmlschema.validators.exceptions import XMLSchemaValidationError

schema = xmlschema.XMLSchema('your-schema.xsd')

xml_file = 'your-file.xml'

try:
    schema.validate(xml_file)
except XMLSchemaValidationError as e:
    print("Validation Error:")
    print(f"Path     : {e.path}")       # XPath to the element with the error
    print(f"Reason   : {e.reason}")     # Human-readable error message
    print(f"Message  : {str(e)}")       # Full formatted message
    print(f"Context  : {e.context}")    # The actual XML data context, if available


Validation Error:
Path     : /root/element/child
Reason   : invalid value 'abc' for xs:date
Message  : failed validating <Element 'child' at 0x...>: invalid value 'abc' for xs:date
Context  : <Element 'child' at 0x...>


errors = list(schema.iter_errors(xml_file))
for err in errors:
    print(f"Path    : {err.path}")
    print(f"Reason  : {err.reason}")
    print(f"Context : {err.context}")
    print("---")
  
