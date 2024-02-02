ANTLR runtime and generated code versions disagree: 4.13.1!=4.10.1
ANTLR runtime and generated code versions disagree: 4.13.1!=4.10.1
 PARAMARRAY:  None
 BYVAL:  None
 BYREF:  None
 PARAMARRAY:  None
 BYVAL:  ByVal
 BYREF:  None
 PARAMARRAY:  None
 BYVAL:  None
 BYREF:  ByRef
 PARAMARRAY:  None
 BYVAL:  ByVal
 BYREF:  None
*************
 {  -  token:322 - (402,) : Rule:48
Text: Public Function GmtDate(Optional ByVal startngDate As Variant                      ) As Date
    On Error GoTo ErrH
    
    Dim diff&: diff = GmtTimeDifference
    
    If IsMissing(startngDate) Then startngDate = Now
    
    GmtDate = DateAdd("s", -diff, startngDate)
    
ErrH: Blame "GmtDate"
End Function
 PARAMARRAY:  None
 BYVAL:  ByVal
 BYREF:  None
*************
 {  -  token:416 - (523,) : Rule:48
Text: Public Function GmtTimeDifference() As Long
    Dim tz As TIME_ZONE_INFORMATION, retCode&
    
    
    
    retCode = GetTimeZoneInformation(tz)
    
    
    
    GmtTimeDifference = -tz.Bias * 60
    
    
    
    If retCode = TIME_ZONE_ID_DAYLIGHT& Then
        
        
        If tz.DaylightDate.wMonth <> 0 Then GmtTimeDifference            = GmtTimeDifference - tz.DaylightBias * 60
    End If
    
ErrH: Blame "GmtTimeDifference"
End Function
*************
 {  -  token:534 - (582,) : Rule:48
Text: Public Function GmtDateLocal(gmtRefernceDate As Date) As Date
    On Error GoTo ErrH
    
    GmtDateLocal = DateAdd("s", GmtTimeDifference(), gmtRefernceDate)
    
ErrH: Blame "GmtDateLocal"
End Function
 PARAMARRAY:  None
 BYVAL:  None
 BYREF:  None
*************
 {  -  token:602 - (689,) : Rule:48
Text: Public Function GmtStringToDate(ByVal internetDateStr As String                              ) As Date
    On Error GoTo ErrH
    
    internetDateStr = Trim$(internetDateStr)
    
    If Mid$(DateString, 11, 1) = "T" Then
        GmtStringToDate = Iso8601TimeToLocalVbTime(internetDateStr)
    Else
        GmtStringToDate = Rfc822TimeToLocalVbTime(internetDateStr)
    End If
    
ErrH: Blame "GmtStringToDate"
End Function
 PARAMARRAY:  None
 BYVAL:  ByVal
 BYREF:  None
*************
 {  -  token:693 - (764,) : Rule:48
Text: Public Function GmtFormat(dateObj As Date                        , Optional dateFormt$ = "ddd, dd mmm yyyy hh:nn:ss"                        , Optional gmtSuffx$ = " GMT"                        ) As String
    On Error GoTo ErrH
    
    GmtFormat = Format$(dateObj, dateFormt) & gmtSuffx
    
ErrH: Blame "GmtFormat"
End Function
 PARAMARRAY:  None
 BYVAL:  None
 BYREF:  None
 PARAMARRAY:  None
 BYVAL:  None
 BYREF:  None
 PARAMARRAY:  None
 BYVAL:  None
 BYREF:  None
*************
 {  -  token:769 - (1187,) : Rule:48
Text: Private Function Iso8601TimeToLocalVbTime(ByVal sIso8601 As String) As Date

    
    
    
    
    
    
    

    
    
    Dim sYear As String
    Dim sMonth As String

    Dim sDay As String
    Dim sHour As String
    Dim sMinute As String

    Dim sSecond As String
    Dim sTimeZone As String
    Dim dtDateTime As Date

    Dim bSign As Boolean
    Dim dGMT As Long

    sYear = Left$(sIso8601, 4)
    sMonth = Mid$(sIso8601, 6, 2)
    sDay = Mid$(sIso8601, 9, 2)
    sHour = Mid$(sIso8601, 12, 2)
    sMinute = Mid$(sIso8601, 15, 2)
    sSecond = Mid$(sIso8601, 18, 2)
    sTimeZone = Mid$(sIso8601, 20)
    
    dtDateTime = CDate(DateSerial(sYear, sMonth, sDay) & " " &                                     TimeSerial(sHour, sMinute, sSecond))
                                     
                                         
    
    sTimeZone = Replace(sTimeZone, "Z", "+00:00", , , vbTextCompare)
    
    
    bSign = IIf(Left$(sTimeZone, 1) = "+", True, False)
    

    
    dGMT = Val(Mid$(sTimeZone, Len(sTimeZone) - 3, 2)) + (CInt(Right$(sTimeZone, 2)) * 100 / 60)
    
    If bSign Then
        dtDateTime = DateAdd("H", -dGMT, dtDateTime)
    Else

        dtDateTime = DateAdd("H", dGMT, dtDateTime)
    End If
    
    Iso8601TimeToLocalVbTime = GmtDateLocal(dtDateTime)
    
    
    
End Function
 PARAMARRAY:  None
 BYVAL:  ByVal
 BYREF:  None
*************
 {  -  token:1190 - (1724,) : Rule:48
Text: Private Function Rfc822TimeToLocalVbTime(sRfc822 As String) As Date

    Dim uSystemTime As SYSTEMTIME
    Dim sWWW As String
    Dim iHours As Integer

    Dim dGMT As Long
    Dim sHourDifferential As String
    Dim dtDateTime As Date

    
    Dim sSign As String
    Dim bSign As Boolean
    Dim sEscapedTime As String

    Dim sTimeZoneString As String
    Dim iPos As Integer
    

    
    
    
    
    sWWW = sRfc822
    
    If InStr(1, sWWW, "GMT", vbTextCompare) > 0 Then
        sWWW = Replace(sWWW, "GMT", "+0000")
    End If

    

    If Len(Trim$(sWWW)) = 25 Then
        
        sWWW = sWWW & " +0000"
    End If

    
    If (InStr(1, sWWW, ",") = 0) Then sWWW = "Thu, " & sWWW
    Call InternetTimeToSystemTime(sWWW, uSystemTime, 0&)
    With uSystemTime
        dtDateTime = CDate(DateSerial(.wYear, .wMonth, .wDay) & " " &                                     TimeSerial(.wHour, .wMinute, .wSecond))
    End With

    
    
    
    sEscapedTime = Replace(sWWW, ":", "")
    
    sSign = Mid$(sEscapedTime, Len(sEscapedTime) - 4, 1)
    bSign = IIf(sSign = "-", False, True)
    
    

    iPos = InStrRev(sWWW, " ")
    If iPos > 0 Then
        
        sTimeZoneString = Mid$(sWWW, iPos + 2)
        
        
        sTimeZoneString = Replace(sTimeZoneString, ":", "")
        sTimeZoneString = Replace(sTimeZoneString, " ", "")
        

        
        dGMT = Val(Left$(sTimeZoneString, 2)) + Val(Right$(sWWW, 2)) * 100 / 60
        
        
    Else
        dGMT = 0
    End If

        
        
    If bSign Then
        dtDateTime = DateAdd("H", -dGMT, dtDateTime)
    Else
        dtDateTime = DateAdd("H", dGMT, dtDateTime)
    End If
    
    Rfc822TimeToLocalVbTime = GmtDateLocal(dtDateTime)
    

End Function
 PARAMARRAY:  None
 BYVAL:  None
 BYREF:  None
 PARAMARRAY:  None
 BYVAL:  None
 BYREF:  None
 PARAMARRAY:  None
 BYVAL:  None
 BYREF:  None
 PARAMARRAY:  None
 BYVAL:  None
 BYREF:  None
 PARAMARRAY:  None
 BYVAL:  None
 BYREF:  None
 PARAMARRAY:  None
 BYVAL:  None
 BYREF:  None
 PARAMARRAY:  None
 BYVAL:  None
 BYREF:  None
 PARAMARRAY:  None
 BYVAL:  ByVal
 BYREF:  None
 PARAMARRAY:  None
 BYVAL:  ByVal
 BYREF:  None
 PARAMARRAY:  None
 BYVAL:  ByVal
 BYREF:  None
 PARAMARRAY:  None
 BYVAL:  ByVal
 BYREF:  None
 PARAMARRAY:  None
 BYVAL:  ByVal
 BYREF:  None
 PARAMARRAY:  None
 BYVAL:  ByVal
 BYREF:  None
{'root': {'args': {'currntProcedure': {'as_type': 'As String',
                                       'has_default': None,
                                       'name': 'currntProcedure',
                                       'optional': None,
                                       'scope': '',
                                       'type_hint': None},
                   'dwReserved': {'as_type': 'As Long',
                                  'has_default': None,
                                  'name': 'dwReserved',
                                  'optional': None,
                                  'scope': '',
                                  'type_hint': None},
                   'errCondition': {'as_type': 'As Boolean',
                                    'has_default': None,
                                    'name': 'errCondition',
                                    'optional': None,
                                    'scope': '',
                                    'type_hint': None},
                   'errSource': {'as_type': 'As String',
                                 'has_default': None,
                                 'name': 'errSource',
                                 'optional': 'Optional',
                                 'scope': '',
                                 'type_hint': None},
                   'errorDescrption': {'as_type': 'As String',
                                       'has_default': None,
                                       'name': 'errorDescrption',
                                       'optional': 'Optional',
                                       'scope': '',
                                       'type_hint': None},
                   'errorMsg': {'as_type': 'As String',
                                'has_default': None,
                                'name': 'errorMsg',
                                'optional': None,
                                'scope': '',
                                'type_hint': None},
                   'errorNumbr': {'as_type': 'As GmtDateTimeErrors',
                                  'default': '= -1',
                                  'has_default': True,
                                  'name': 'errorNumbr',
                                  'optional': 'Optional',
                                  'scope': '',
                                  'type_hint': None},
                   'lpTimeZoneInformation': {'as_type': 'As '
                                                        'TIME_ZONE_INFORMATION',
                                             'has_default': None,
                                             'name': 'lpTimeZoneInformation',
                                             'optional': None,
                                             'scope': '',
                                             'type_hint': None},
                   'lpszTime': {'as_type': 'As String',
                                'has_default': None,
                                'name': 'lpszTime',
                                'optional': None,
                                'scope': '',
                                'type_hint': None},
                   'pst': {'as_type': 'As SYSTEMTIME',
                           'has_default': None,
                           'name': 'pst',
                           'optional': None,
                           'scope': '',
                           'type_hint': None}},
          'func': {'GmtDate': {'args': {'startngDate': {'as_type': 'As Variant',
                                                        'has_default': None,
                                                        'name': 'startngDate',
                                                        'optional': 'Optional',
                                                        'scope': 'GmtDate',
                                                        'type_hint': None}},
                               'col': None,
                               'end': None,
                               'name': 'GmtDate',
                               'start': None},
                   'GmtDateLocal': {'args': {'gmtRefernceDate': {'as_type': 'As '
                                                                            'Date',
                                                                 'has_default': None,
                                                                 'name': 'gmtRefernceDate',
                                                                 'optional': None,
                                                                 'scope': 'GmtDateLocal',
                                                                 'type_hint': None}},
                                    'col': None,
                                    'end': None,
                                    'name': 'GmtDateLocal',
                                    'start': None},
                   'GmtFormat': {'args': {'dateFormt': {'as_type': None,
                                                        'default': '= "ddd, dd '
                                                                   'mmm yyyy '
                                                                   'hh:nn:ss"',
                                                        'has_default': True,
                                                        'name': 'dateFormt',
                                                        'optional': 'Optional',
                                                        'scope': 'GmtFormat',
                                                        'type_hint': '$'},
                                          'dateObj': {'as_type': 'As Date',
                                                      'has_default': None,
                                                      'name': 'dateObj',
                                                      'optional': None,
                                                      'scope': 'GmtFormat',
                                                      'type_hint': None},
                                          'gmtSuffx': {'as_type': None,
                                                       'default': '= " GMT"',
                                                       'has_default': True,
                                                       'name': 'gmtSuffx',
                                                       'optional': 'Optional',
                                                       'scope': 'GmtFormat',
                                                       'type_hint': '$'}},
                                 'col': None,
                                 'end': None,
                                 'name': 'GmtFormat',
                                 'start': None},
                   'GmtStringToDate': {'args': {'internetDateStr': {'as_type': 'As '
                                                                               'String',
                                                                    'has_default': None,
                                                                    'name': 'internetDateStr',
                                                                    'optional': None,
                                                                    'scope': 'GmtStringToDate',
                                                                    'type_hint': None}},
                                       'col': None,
                                       'end': None,
                                       'name': 'GmtStringToDate',
                                       'start': None},
                   'GmtTimeDifference': {'col': None,
                                         'end': None,
                                         'name': 'GmtTimeDifference',
                                         'start': None},
                   'Iso8601TimeToLocalVbTime': {'args': {'sIso8601': {'as_type': 'As '
                                                                                 'String',
                                                                      'has_default': None,
                                                                      'name': 'sIso8601',
                                                                      'optional': None,
                                                                      'scope': 'Iso8601TimeToLocalVbTime',
                                                                      'type_hint': None}},
                                                'col': None,
                                                'end': None,
                                                'name': 'Iso8601TimeToLocalVbTime',
                                                'start': None},
                   'Rfc822TimeToLocalVbTime': {'args': {'sRfc822': {'as_type': 'As '
                                                                               'String',
                                                                    'has_default': None,
                                                                    'name': 'sRfc822',
                                                                    'optional': None,
                                                                    'scope': 'Rfc822TimeToLocalVbTime',
                                                                    'type_hint': None}},
                                               'col': None,
                                               'end': None,
                                               'name': 'Rfc822TimeToLocalVbTime',
                                               'start': None}}}}
