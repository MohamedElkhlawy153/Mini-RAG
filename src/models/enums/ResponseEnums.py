from enum import Enum

class ResponseSignal(Enum):
    File_Validation_Passed = "File validation passed"
    File_Type_Not_Allowed = "File type not allowed"
    File_Size_Exceeds_Limit = "File size exceeds the limit"
    File_uploaded_Successfully = "File uploaded successfully"
    File_Failed = "File upload failed"
    File_Processing_Failed = "File processing failed"
    File_Chunks_Generated = "File chunks generated"

