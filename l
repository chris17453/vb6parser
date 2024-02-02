ANTLR runtime and generated code versions disagree: 4.13.1!=4.10.1
ANTLR runtime and generated code versions disagree: 4.13.1!=4.10.1
*************
 {  -  token:2 - (2,) : Rule:139
Text: VB_Name
*************
 {  -  token:18 - (18,) : Rule:139
Text: GmtDateTimeErrors
*************
 {  -  token:20 - (20,) : Rule:139
Text: ErrorBase
*************
 {  -  token:24 - (24,) : Rule:139
Text: vbObjectError
*************
 {  -  token:30 - (30,) : Rule:139
Text: NotInitted
*************
 {  -  token:32 - (32,) : Rule:139
Text: AlreadyInitted
*************
 {  -  token:42 - (42,) : Rule:139
Text: ErrorHolder
*************
 {  -  token:44 - (44,) : Rule:139
Text: HasError
*************
 {  -  token:50 - (50,) : Rule:139
Text: Source
*************
 {  -  token:56 - (56,) : Rule:139
Text: Number
*************
 {  -  token:60 - (60,) : Rule:139
Text: GmtDateTimeErrors
*************
 {  -  token:62 - (62,) : Rule:139
Text: Description
*************
 {  -  token:72 - (72,) : Rule:139
Text: mError
*************
 {  -  token:76 - (76,) : Rule:139
Text: ErrorHolder
*************
 {  -  token:84 - (84,) : Rule:139
Text: SYSTEMTIME
*************
 {  -  token:86 - (86,) : Rule:139
Text: wYear
*************
 {  -  token:92 - (92,) : Rule:139
Text: wMonth
*************
 {  -  token:99 - (99,) : Rule:139
Text: wDayOfWeek
*************
 {  -  token:105 - (105,) : Rule:139
Text: wDay
*************
 {  -  token:111 - (111,) : Rule:139
Text: wHour
*************
 {  -  token:118 - (118,) : Rule:139
Text: wMinute
*************
 {  -  token:124 - (124,) : Rule:139
Text: wSecond
*************
 {  -  token:130 - (130,) : Rule:139
Text: wMilliseconds
*************
 {  -  token:144 - (144,) : Rule:139
Text: TIME_ZONE_INFORMATION
*************
 {  -  token:146 - (146,) : Rule:139
Text: Bias
*************
 {  -  token:152 - (152,) : Rule:139
Text: StandardName
*************
 {  -  token:162 - (162,) : Rule:139
Text: StandardDate
*************
 {  -  token:166 - (166,) : Rule:139
Text: SYSTEMTIME
*************
 {  -  token:168 - (168,) : Rule:139
Text: StandardBias
*************
 {  -  token:174 - (174,) : Rule:139
Text: DaylightName
*************
 {  -  token:183 - (183,) : Rule:139
Text: DaylightDate
*************
 {  -  token:187 - (187,) : Rule:139
Text: SYSTEMTIME
*************
 {  -  token:189 - (189,) : Rule:139
Text: DaylightBias
*************
 {  -  token:205 - (205,) : Rule:139
Text: GetTimeZoneInformation
*************
 {  -  token:211 - (217,) : Rule:134
Text: (lpTimeZoneInformation As TIME_ZONE_INFORMATION)
*************
  {  -  token:212 - (216,) : Rule:135
Text: lpTimeZoneInformation As TIME_ZONE_INFORMATION
*************
   {  -  token:212 - (212,) : Rule:139
Text: lpTimeZoneInformation
*************
   {  -  token:216 - (216,) : Rule:139
Text: TIME_ZONE_INFORMATION
*************
 {  -  token:228 - (228,) : Rule:139
Text: TIME_ZONE_ID_INVALID
*************
 {  -  token:239 - (239,) : Rule:139
Text: TIME_ZONE_ID_STANDARD
*************
 {  -  token:250 - (250,) : Rule:139
Text: TIME_ZONE_ID_UNKNOWN
*************
 {  -  token:262 - (262,) : Rule:139
Text: TIME_ZONE_ID_DAYLIGHT
*************
 {  -  token:277 - (277,) : Rule:139
Text: InternetTimeToSystemTime
*************
 {  -  token:283 - (309,) : Rule:134
Text: (ByVal lpszTime As String,        ByRef pst As SYSTEMTIME,        ByVal dwReserved As Long)
*************
  {  -  token:284 - (290,) : Rule:135
Text: ByVal lpszTime As String
*************
   {  -  token:286 - (286,) : Rule:139
Text: lpszTime
*************
  {  -  token:293 - (299,) : Rule:135
Text: ByRef pst As SYSTEMTIME
*************
   {  -  token:295 - (295,) : Rule:139
Text: pst
*************
   {  -  token:299 - (299,) : Rule:139
Text: SYSTEMTIME
*************
  {  -  token:302 - (308,) : Rule:135
Text: ByVal dwReserved As Long
*************
   {  -  token:304 - (304,) : Rule:139
Text: dwReserved
*************
 {  -  token:322 - (402,) : Rule:48
Text: Public Function GmtDate(Optional ByVal startngDate As Variant                      ) As Date
    On Error GoTo ErrH
    
    Dim diff&: diff = GmtTimeDifference
    
    If IsMissing(startngDate) Then startngDate = Now
    
    GmtDate = DateAdd("s", -diff, startngDate)
    
ErrH: Blame "GmtDate"
End Function
*************
  {  -  token:326 - (326,) : Rule:139
Text: GmtDate
*************
  {  -  token:327 - (338,) : Rule:134
Text: (Optional ByVal startngDate As Variant                      )
*************
   {  -  token:328 - (336,) : Rule:135
Text: Optional ByVal startngDate As Variant
*************
    {  -  token:332 - (332,) : Rule:139
Text: startngDate
*************
  {  -  token:348 - (348,) : Rule:139
Text: ErrH
*************
  {  -  token:353 - (353,) : Rule:139
Text: diff
*************
  {  -  token:356 - (356,) : Rule:139
Text: diff
*************
  {  -  token:360 - (360,) : Rule:139
Text: GmtTimeDifference
*************
  {  -  token:365 - (365,) : Rule:139
Text: IsMissing
*************
  {  -  token:367 - (367,) : Rule:139
Text: startngDate
*************
  {  -  token:372 - (372,) : Rule:139
Text: startngDate
*************
  {  -  token:376 - (376,) : Rule:139
Text: Now
*************
  {  -  token:379 - (379,) : Rule:139
Text: GmtDate
*************
  {  -  token:383 - (383,) : Rule:139
Text: DateAdd
*************
  {  -  token:389 - (389,) : Rule:139
Text: diff
*************
  {  -  token:392 - (392,) : Rule:139
Text: startngDate
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
  {  -  token:420 - (420,) : Rule:139
Text: GmtTimeDifference
*************
  {  -  token:421 - (422,) : Rule:134
Text: ()
*************
  {  -  token:430 - (430,) : Rule:139
Text: tz
*************
  {  -  token:434 - (434,) : Rule:139
Text: TIME_ZONE_INFORMATION
*************
  {  -  token:437 - (437,) : Rule:139
Text: retCode
*************
  {  -  token:443 - (443,) : Rule:139
Text: retCode
*************
  {  -  token:447 - (447,) : Rule:139
Text: GetTimeZoneInformation
*************
  {  -  token:449 - (449,) : Rule:139
Text: tz
*************
  {  -  token:455 - (455,) : Rule:139
Text: GmtTimeDifference
*************
  {  -  token:460 - (460,) : Rule:139
Text: tz
*************
  {  -  token:462 - (462,) : Rule:139
Text: Bias
*************
  {  -  token:473 - (473,) : Rule:139
Text: retCode
*************
  {  -  token:477 - (477,) : Rule:139
Text: TIME_ZONE_ID_DAYLIGHT
*************
  {  -  token:486 - (486,) : Rule:139
Text: tz
*************
  {  -  token:488 - (488,) : Rule:139
Text: DaylightDate
*************
  {  -  token:490 - (490,) : Rule:139
Text: wMonth
*************
  {  -  token:498 - (498,) : Rule:139
Text: GmtTimeDifference
*************
  {  -  token:502 - (502,) : Rule:139
Text: GmtTimeDifference
*************
  {  -  token:506 - (506,) : Rule:139
Text: tz
*************
  {  -  token:508 - (508,) : Rule:139
Text: DaylightBias
*************
 {  -  token:534 - (582,) : Rule:48
Text: Public Function GmtDateLocal(gmtRefernceDate As Date) As Date
    On Error GoTo ErrH
    
    GmtDateLocal = DateAdd("s", GmtTimeDifference(), gmtRefernceDate)
    
ErrH: Blame "GmtDateLocal"
End Function
*************
  {  -  token:538 - (538,) : Rule:139
Text: GmtDateLocal
*************
  {  -  token:539 - (545,) : Rule:134
Text: (gmtRefernceDate As Date)
*************
   {  -  token:540 - (544,) : Rule:135
Text: gmtRefernceDate As Date
*************
    {  -  token:540 - (540,) : Rule:139
Text: gmtRefernceDate
*************
  {  -  token:555 - (555,) : Rule:139
Text: ErrH
*************
  {  -  token:558 - (558,) : Rule:139
Text: GmtDateLocal
*************
  {  -  token:562 - (562,) : Rule:139
Text: DateAdd
*************
  {  -  token:567 - (567,) : Rule:139
Text: GmtTimeDifference
*************
  {  -  token:572 - (572,) : Rule:139
Text: gmtRefernceDate
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
*************
  {  -  token:606 - (606,) : Rule:139
Text: GmtStringToDate
*************
  {  -  token:607 - (616,) : Rule:134
Text: (ByVal internetDateStr As String                              )
*************
   {  -  token:608 - (614,) : Rule:135
Text: ByVal internetDateStr As String
*************
    {  -  token:610 - (610,) : Rule:139
Text: internetDateStr
*************
  {  -  token:626 - (626,) : Rule:139
Text: ErrH
*************
  {  -  token:629 - (629,) : Rule:139
Text: internetDateStr
*************
  {  -  token:633 - (633,) : Rule:139
Text: Trim
*************
  {  -  token:636 - (636,) : Rule:139
Text: internetDateStr
*************
  {  -  token:642 - (642,) : Rule:139
Text: Mid
*************
  {  -  token:645 - (645,) : Rule:139
Text: DateString
*************
  {  -  token:660 - (660,) : Rule:139
Text: GmtStringToDate
*************
  {  -  token:664 - (664,) : Rule:139
Text: Iso8601TimeToLocalVbTime
*************
  {  -  token:666 - (666,) : Rule:139
Text: internetDateStr
*************
  {  -  token:671 - (671,) : Rule:139
Text: GmtStringToDate
*************
  {  -  token:675 - (675,) : Rule:139
Text: Rfc822TimeToLocalVbTime
*************
  {  -  token:677 - (677,) : Rule:139
Text: internetDateStr
*************
 {  -  token:693 - (764,) : Rule:48
Text: Public Function GmtFormat(dateObj As Date                        , Optional dateFormt$ = "ddd, dd mmm yyyy hh:nn:ss"                        , Optional gmtSuffx$ = " GMT"                        ) As String
    On Error GoTo ErrH
    
    GmtFormat = Format$(dateObj, dateFormt) & gmtSuffx
    
ErrH: Blame "GmtFormat"
End Function
*************
  {  -  token:697 - (697,) : Rule:139
Text: GmtFormat
*************
  {  -  token:698 - (727,) : Rule:134
Text: (dateObj As Date                        , Optional dateFormt$ = "ddd, dd mmm yyyy hh:nn:ss"                        , Optional gmtSuffx$ = " GMT"                        )
*************
   {  -  token:699 - (703,) : Rule:135
Text: dateObj As Date
*************
    {  -  token:699 - (699,) : Rule:139
Text: dateObj
*************
   {  -  token:707 - (714,) : Rule:135
Text: Optional dateFormt$ = "ddd, dd mmm yyyy hh:nn:ss"
*************
    {  -  token:709 - (709,) : Rule:139
Text: dateFormt
DEFAULT VALUE -'GmtFormat' : = "ddd, dd mmm yyyy hh:nn:ss"
*************
    {  -  token:712 - (714,) : Rule:136
Text: = "ddd, dd mmm yyyy hh:nn:ss"
*************
   {  -  token:718 - (725,) : Rule:135
Text: Optional gmtSuffx$ = " GMT"
*************
    {  -  token:720 - (720,) : Rule:139
Text: gmtSuffx
DEFAULT VALUE -'GmtFormat' : = " GMT"
*************
    {  -  token:723 - (725,) : Rule:136
Text: = " GMT"
*************
  {  -  token:737 - (737,) : Rule:139
Text: ErrH
*************
  {  -  token:740 - (740,) : Rule:139
Text: GmtFormat
*************
  {  -  token:744 - (744,) : Rule:139
Text: Format
*************
  {  -  token:747 - (747,) : Rule:139
Text: dateObj
*************
  {  -  token:750 - (750,) : Rule:139
Text: dateFormt
*************
  {  -  token:755 - (755,) : Rule:139
Text: gmtSuffx
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
*************
  {  -  token:773 - (773,) : Rule:139
Text: Iso8601TimeToLocalVbTime
*************
  {  -  token:774 - (782,) : Rule:134
Text: (ByVal sIso8601 As String)
*************
   {  -  token:775 - (781,) : Rule:135
Text: ByVal sIso8601 As String
*************
    {  -  token:777 - (777,) : Rule:139
Text: sIso8601
*************
  {  -  token:801 - (801,) : Rule:139
Text: sYear
*************
  {  -  token:809 - (809,) : Rule:139
Text: sMonth
*************
  {  -  token:818 - (818,) : Rule:139
Text: sDay
*************
  {  -  token:826 - (826,) : Rule:139
Text: sHour
*************
  {  -  token:834 - (834,) : Rule:139
Text: sMinute
*************
  {  -  token:843 - (843,) : Rule:139
Text: sSecond
*************
  {  -  token:851 - (851,) : Rule:139
Text: sTimeZone
*************
  {  -  token:859 - (859,) : Rule:139
Text: dtDateTime
*************
  {  -  token:868 - (868,) : Rule:139
Text: bSign
*************
  {  -  token:876 - (876,) : Rule:139
Text: dGMT
*************
  {  -  token:883 - (883,) : Rule:139
Text: sYear
*************
  {  -  token:887 - (887,) : Rule:139
Text: Left
*************
  {  -  token:890 - (890,) : Rule:139
Text: sIso8601
*************
  {  -  token:896 - (896,) : Rule:139
Text: sMonth
*************
  {  -  token:900 - (900,) : Rule:139
Text: Mid
*************
  {  -  token:903 - (903,) : Rule:139
Text: sIso8601
*************
  {  -  token:912 - (912,) : Rule:139
Text: sDay
*************
  {  -  token:916 - (916,) : Rule:139
Text: Mid
*************
  {  -  token:919 - (919,) : Rule:139
Text: sIso8601
*************
  {  -  token:928 - (928,) : Rule:139
Text: sHour
*************
  {  -  token:932 - (932,) : Rule:139
Text: Mid
*************
  {  -  token:935 - (935,) : Rule:139
Text: sIso8601
*************
  {  -  token:944 - (944,) : Rule:139
Text: sMinute
*************
  {  -  token:948 - (948,) : Rule:139
Text: Mid
*************
  {  -  token:951 - (951,) : Rule:139
Text: sIso8601
*************
  {  -  token:960 - (960,) : Rule:139
Text: sSecond
*************
  {  -  token:964 - (964,) : Rule:139
Text: Mid
*************
  {  -  token:967 - (967,) : Rule:139
Text: sIso8601
*************
  {  -  token:976 - (976,) : Rule:139
Text: sTimeZone
*************
  {  -  token:980 - (980,) : Rule:139
Text: Mid
*************
  {  -  token:983 - (983,) : Rule:139
Text: sIso8601
*************
  {  -  token:990 - (990,) : Rule:139
Text: dtDateTime
*************
  {  -  token:994 - (994,) : Rule:139
Text: CDate
*************
  {  -  token:996 - (996,) : Rule:139
Text: DateSerial
*************
  {  -  token:998 - (998,) : Rule:139
Text: sYear
*************
  {  -  token:1001 - (1001,) : Rule:139
Text: sMonth
*************
  {  -  token:1004 - (1004,) : Rule:139
Text: sDay
*************
  {  -  token:1013 - (1013,) : Rule:139
Text: TimeSerial
*************
  {  -  token:1015 - (1015,) : Rule:139
Text: sHour
*************
  {  -  token:1018 - (1018,) : Rule:139
Text: sMinute
*************
  {  -  token:1021 - (1021,) : Rule:139
Text: sSecond
*************
  {  -  token:1028 - (1028,) : Rule:139
Text: sTimeZone
*************
  {  -  token:1032 - (1032,) : Rule:139
Text: Replace
*************
  {  -  token:1034 - (1034,) : Rule:139
Text: sTimeZone
*************
  {  -  token:1047 - (1047,) : Rule:139
Text: vbTextCompare
*************
  {  -  token:1052 - (1052,) : Rule:139
Text: bSign
*************
  {  -  token:1056 - (1056,) : Rule:139
Text: IIf
*************
  {  -  token:1058 - (1058,) : Rule:139
Text: Left
*************
  {  -  token:1061 - (1061,) : Rule:139
Text: sTimeZone
*************
  {  -  token:1081 - (1081,) : Rule:139
Text: dGMT
*************
  {  -  token:1085 - (1085,) : Rule:139
Text: Val
*************
  {  -  token:1087 - (1087,) : Rule:139
Text: Mid
*************
  {  -  token:1090 - (1090,) : Rule:139
Text: sTimeZone
*************
  {  -  token:1093 - (1093,) : Rule:139
Text: Len
*************
  {  -  token:1095 - (1095,) : Rule:139
Text: sTimeZone
*************
  {  -  token:1110 - (1110,) : Rule:139
Text: CInt
*************
  {  -  token:1112 - (1112,) : Rule:139
Text: Right
*************
  {  -  token:1115 - (1115,) : Rule:139
Text: sTimeZone
*************
  {  -  token:1134 - (1134,) : Rule:139
Text: bSign
*************
  {  -  token:1138 - (1138,) : Rule:139
Text: dtDateTime
*************
  {  -  token:1142 - (1142,) : Rule:139
Text: DateAdd
*************
  {  -  token:1148 - (1148,) : Rule:139
Text: dGMT
*************
  {  -  token:1151 - (1151,) : Rule:139
Text: dtDateTime
*************
  {  -  token:1157 - (1157,) : Rule:139
Text: dtDateTime
*************
  {  -  token:1161 - (1161,) : Rule:139
Text: DateAdd
*************
  {  -  token:1166 - (1166,) : Rule:139
Text: dGMT
*************
  {  -  token:1169 - (1169,) : Rule:139
Text: dtDateTime
*************
  {  -  token:1175 - (1175,) : Rule:139
Text: Iso8601TimeToLocalVbTime
*************
  {  -  token:1179 - (1179,) : Rule:139
Text: GmtDateLocal
*************
  {  -  token:1181 - (1181,) : Rule:139
Text: dtDateTime
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
*************
  {  -  token:1194 - (1194,) : Rule:139
Text: Rfc822TimeToLocalVbTime
*************
  {  -  token:1195 - (1201,) : Rule:134
Text: (sRfc822 As String)
*************
   {  -  token:1196 - (1200,) : Rule:135
Text: sRfc822 As String
*************
    {  -  token:1196 - (1196,) : Rule:139
Text: sRfc822
*************
  {  -  token:1210 - (1210,) : Rule:139
Text: uSystemTime
*************
  {  -  token:1214 - (1214,) : Rule:139
Text: SYSTEMTIME
*************
  {  -  token:1218 - (1218,) : Rule:139
Text: sWWW
*************
  {  -  token:1226 - (1226,) : Rule:139
Text: iHours
*************
  {  -  token:1235 - (1235,) : Rule:139
Text: dGMT
*************
  {  -  token:1243 - (1243,) : Rule:139
Text: sHourDifferential
*************
  {  -  token:1251 - (1251,) : Rule:139
Text: dtDateTime
*************
  {  -  token:1261 - (1261,) : Rule:139
Text: sSign
*************
  {  -  token:1269 - (1269,) : Rule:139
Text: bSign
*************
  {  -  token:1277 - (1277,) : Rule:139
Text: sEscapedTime
*************
  {  -  token:1286 - (1286,) : Rule:139
Text: sTimeZoneString
*************
  {  -  token:1294 - (1294,) : Rule:139
Text: iPos
*************
  {  -  token:1306 - (1306,) : Rule:139
Text: sWWW
*************
  {  -  token:1310 - (1310,) : Rule:139
Text: sRfc822
*************
  {  -  token:1315 - (1315,) : Rule:139
Text: InStr
*************
  {  -  token:1320 - (1320,) : Rule:139
Text: sWWW
*************
  {  -  token:1326 - (1326,) : Rule:139
Text: vbTextCompare
*************
  {  -  token:1335 - (1335,) : Rule:139
Text: sWWW
*************
  {  -  token:1339 - (1339,) : Rule:139
Text: Replace
*************
  {  -  token:1341 - (1341,) : Rule:139
Text: sWWW
*************
  {  -  token:1357 - (1357,) : Rule:139
Text: Len
*************
  {  -  token:1359 - (1359,) : Rule:139
Text: Trim
*************
  {  -  token:1362 - (1362,) : Rule:139
Text: sWWW
*************
  {  -  token:1373 - (1373,) : Rule:139
Text: sWWW
*************
  {  -  token:1377 - (1377,) : Rule:139
Text: sWWW
*************
  {  -  token:1390 - (1390,) : Rule:139
Text: InStr
*************
  {  -  token:1395 - (1395,) : Rule:139
Text: sWWW
*************
  {  -  token:1408 - (1408,) : Rule:139
Text: sWWW
*************
  {  -  token:1416 - (1416,) : Rule:139
Text: sWWW
*************
  {  -  token:1420 - (1420,) : Rule:139
Text: InternetTimeToSystemTime
*************
  {  -  token:1422 - (1422,) : Rule:139
Text: sWWW
*************
  {  -  token:1425 - (1425,) : Rule:139
Text: uSystemTime
*************
  {  -  token:1433 - (1433,) : Rule:139
Text: uSystemTime
*************
  {  -  token:1435 - (1435,) : Rule:139
Text: dtDateTime
*************
  {  -  token:1439 - (1439,) : Rule:139
Text: CDate
*************
  {  -  token:1441 - (1441,) : Rule:139
Text: DateSerial
*************
  {  -  token:1444 - (1444,) : Rule:139
Text: wYear
*************
  {  -  token:1448 - (1448,) : Rule:139
Text: wMonth
*************
  {  -  token:1452 - (1452,) : Rule:139
Text: wDay
*************
  {  -  token:1461 - (1461,) : Rule:139
Text: TimeSerial
*************
  {  -  token:1464 - (1464,) : Rule:139
Text: wHour
*************
  {  -  token:1468 - (1468,) : Rule:139
Text: wMinute
*************
  {  -  token:1472 - (1472,) : Rule:139
Text: wSecond
*************
  {  -  token:1482 - (1482,) : Rule:139
Text: sEscapedTime
*************
  {  -  token:1486 - (1486,) : Rule:139
Text: Replace
*************
  {  -  token:1488 - (1488,) : Rule:139
Text: sWWW
*************
  {  -  token:1498 - (1498,) : Rule:139
Text: sSign
*************
  {  -  token:1502 - (1502,) : Rule:139
Text: Mid
*************
  {  -  token:1505 - (1505,) : Rule:139
Text: sEscapedTime
*************
  {  -  token:1508 - (1508,) : Rule:139
Text: Len
*************
  {  -  token:1510 - (1510,) : Rule:139
Text: sEscapedTime
*************
  {  -  token:1521 - (1521,) : Rule:139
Text: bSign
*************
  {  -  token:1525 - (1525,) : Rule:139
Text: IIf
*************
  {  -  token:1527 - (1527,) : Rule:139
Text: sSign
*************
  {  -  token:1543 - (1543,) : Rule:139
Text: iPos
*************
  {  -  token:1547 - (1547,) : Rule:139
Text: InStrRev
*************
  {  -  token:1549 - (1549,) : Rule:139
Text: sWWW
*************
  {  -  token:1557 - (1557,) : Rule:139
Text: iPos
*************
  {  -  token:1566 - (1566,) : Rule:139
Text: sTimeZoneString
*************
  {  -  token:1570 - (1570,) : Rule:139
Text: Mid
*************
  {  -  token:1573 - (1573,) : Rule:139
Text: sWWW
*************
  {  -  token:1576 - (1576,) : Rule:139
Text: iPos
*************
  {  -  token:1585 - (1585,) : Rule:139
Text: sTimeZoneString
*************
  {  -  token:1589 - (1589,) : Rule:139
Text: Replace
*************
  {  -  token:1591 - (1591,) : Rule:139
Text: sTimeZoneString
*************
  {  -  token:1600 - (1600,) : Rule:139
Text: sTimeZoneString
*************
  {  -  token:1604 - (1604,) : Rule:139
Text: Replace
*************
  {  -  token:1606 - (1606,) : Rule:139
Text: sTimeZoneString
*************
  {  -  token:1618 - (1618,) : Rule:139
Text: dGMT
*************
  {  -  token:1622 - (1622,) : Rule:139
Text: Val
*************
  {  -  token:1624 - (1624,) : Rule:139
Text: Left
*************
  {  -  token:1627 - (1627,) : Rule:139
Text: sTimeZoneString
*************
  {  -  token:1636 - (1636,) : Rule:139
Text: Val
*************
  {  -  token:1638 - (1638,) : Rule:139
Text: Right
*************
  {  -  token:1641 - (1641,) : Rule:139
Text: sWWW
*************
  {  -  token:1660 - (1660,) : Rule:139
Text: dGMT
*************
  {  -  token:1673 - (1673,) : Rule:139
Text: bSign
*************
  {  -  token:1677 - (1677,) : Rule:139
Text: dtDateTime
*************
  {  -  token:1681 - (1681,) : Rule:139
Text: DateAdd
*************
  {  -  token:1687 - (1687,) : Rule:139
Text: dGMT
*************
  {  -  token:1690 - (1690,) : Rule:139
Text: dtDateTime
*************
  {  -  token:1695 - (1695,) : Rule:139
Text: dtDateTime
*************
  {  -  token:1699 - (1699,) : Rule:139
Text: DateAdd
*************
  {  -  token:1704 - (1704,) : Rule:139
Text: dGMT
*************
  {  -  token:1707 - (1707,) : Rule:139
Text: dtDateTime
*************
  {  -  token:1713 - (1713,) : Rule:139
Text: Rfc822TimeToLocalVbTime
*************
  {  -  token:1717 - (1717,) : Rule:139
Text: GmtDateLocal
*************
  {  -  token:1719 - (1719,) : Rule:139
Text: dtDateTime
*************
 {  -  token:1742 - (1742,) : Rule:139
Text: ErrRaise
*************
 {  -  token:1743 - (1775,) : Rule:134
Text: (errorMsg As String                   , Optional errorNumbr As GmtDateTimeErrors = -1                   , Optional errSource As String                   )
*************
  {  -  token:1744 - (1748,) : Rule:135
Text: errorMsg As String
*************
   {  -  token:1744 - (1744,) : Rule:139
Text: errorMsg
*************
  {  -  token:1752 - (1763,) : Rule:135
Text: Optional errorNumbr As GmtDateTimeErrors = -1
*************
   {  -  token:1754 - (1754,) : Rule:139
Text: errorNumbr
*************
   {  -  token:1758 - (1758,) : Rule:139
Text: GmtDateTimeErrors
DEFAULT VALUE -'' : = -1
*************
   {  -  token:1760 - (1763,) : Rule:136
Text: = -1
*************
  {  -  token:1767 - (1773,) : Rule:135
Text: Optional errSource As String
*************
   {  -  token:1769 - (1769,) : Rule:139
Text: errSource
*************
 {  -  token:1777 - (1777,) : Rule:139
Text: Err
*************
 {  -  token:1779 - (1779,) : Rule:139
Text: Raise
*************
 {  -  token:1781 - (1781,) : Rule:139
Text: errorNumbr
*************
 {  -  token:1784 - (1784,) : Rule:139
Text: IIf
*************
 {  -  token:1786 - (1786,) : Rule:139
Text: LenB
*************
 {  -  token:1788 - (1788,) : Rule:139
Text: errSource
*************
 {  -  token:1796 - (1796,) : Rule:139
Text: TypeName
*************
 {  -  token:1798 - (1798,) : Rule:139
Text: Me
*************
 {  -  token:1802 - (1802,) : Rule:139
Text: errSource
*************
 {  -  token:1806 - (1806,) : Rule:139
Text: errorMsg
*************
 {  -  token:1815 - (1815,) : Rule:139
Text: ErrorIf
*************
 {  -  token:1816 - (1846,) : Rule:134
Text: (errCondition As Boolean                  , errorMsg As String                  , Optional errorNumbr As GmtDateTimeErrors = -1                  )
*************
  {  -  token:1817 - (1821,) : Rule:135
Text: errCondition As Boolean
*************
   {  -  token:1817 - (1817,) : Rule:139
Text: errCondition
*************
  {  -  token:1825 - (1829,) : Rule:135
Text: errorMsg As String
*************
   {  -  token:1825 - (1825,) : Rule:139
Text: errorMsg
*************
  {  -  token:1833 - (1844,) : Rule:135
Text: Optional errorNumbr As GmtDateTimeErrors = -1
*************
   {  -  token:1835 - (1835,) : Rule:139
Text: errorNumbr
*************
   {  -  token:1839 - (1839,) : Rule:139
Text: GmtDateTimeErrors
DEFAULT VALUE -'' : = -1
*************
   {  -  token:1841 - (1844,) : Rule:136
Text: = -1
*************
 {  -  token:1850 - (1850,) : Rule:139
Text: errCondition
*************
 {  -  token:1856 - (1856,) : Rule:139
Text: errorMsg
*************
 {  -  token:1859 - (1859,) : Rule:139
Text: errorNumbr
*************
 {  -  token:1868 - (1868,) : Rule:139
Text: SaveError
*************
 {  -  token:1869 - (1870,) : Rule:134
Text: ()
*************
 {  -  token:1874 - (1874,) : Rule:139
Text: mError
*************
 {  -  token:1878 - (1878,) : Rule:139
Text: Err
*************
 {  -  token:1883 - (1883,) : Rule:139
Text: HasError
*************
 {  -  token:1890 - (1890,) : Rule:139
Text: Description
*************
 {  -  token:1894 - (1894,) : Rule:139
Text: Err
*************
 {  -  token:1896 - (1896,) : Rule:139
Text: Description
*************
 {  -  token:1899 - (1899,) : Rule:139
Text: Number
*************
 {  -  token:1903 - (1903,) : Rule:139
Text: Err
*************
 {  -  token:1905 - (1905,) : Rule:139
Text: Number
*************
 {  -  token:1908 - (1908,) : Rule:139
Text: Source
*************
 {  -  token:1912 - (1912,) : Rule:139
Text: Err
*************
 {  -  token:1914 - (1914,) : Rule:139
Text: Source
*************
 {  -  token:1920 - (1920,) : Rule:139
Text: HasError
*************
 {  -  token:1927 - (1927,) : Rule:139
Text: Description
*************
 {  -  token:1931 - (1931,) : Rule:139
Text: vbNullString
*************
 {  -  token:1934 - (1934,) : Rule:139
Text: Number
*************
 {  -  token:1941 - (1941,) : Rule:139
Text: Source
*************
 {  -  token:1945 - (1945,) : Rule:139
Text: vbNullString
*************
 {  -  token:1951 - (1951,) : Rule:139
Text: Err
*************
 {  -  token:1953 - (1953,) : Rule:139
Text: Clear
*************
 {  -  token:1962 - (1962,) : Rule:139
Text: Blame
*************
 {  -  token:1963 - (2001,) : Rule:134
Text: (ByVal currntProcedure As String                , Optional ByVal errorDescrption As String                , Optional ByVal errorNumbr As GmtDateTimeErrors = -1                )
*************
  {  -  token:1964 - (1970,) : Rule:135
Text: ByVal currntProcedure As String
*************
   {  -  token:1966 - (1966,) : Rule:139
Text: currntProcedure
*************
  {  -  token:1974 - (1982,) : Rule:135
Text: Optional ByVal errorDescrption As String
*************
   {  -  token:1978 - (1978,) : Rule:139
Text: errorDescrption
*************
  {  -  token:1986 - (1999,) : Rule:135
Text: Optional ByVal errorNumbr As GmtDateTimeErrors = -1
*************
   {  -  token:1990 - (1990,) : Rule:139
Text: errorNumbr
*************
   {  -  token:1994 - (1994,) : Rule:139
Text: GmtDateTimeErrors
DEFAULT VALUE -'' : = -1
*************
   {  -  token:1996 - (1999,) : Rule:136
Text: = -1
*************
 {  -  token:2005 - (2005,) : Rule:139
Text: SaveError
*************
 {  -  token:2009 - (2009,) : Rule:139
Text: LoadError
*************
 {  -  token:2011 - (2011,) : Rule:139
Text: currntProcedure
*************
 {  -  token:2014 - (2014,) : Rule:139
Text: errorDescrption
*************
 {  -  token:2017 - (2017,) : Rule:139
Text: errorNumbr
*************
 {  -  token:2027 - (2027,) : Rule:139
Text: LoadError
*************
 {  -  token:2028 - (2066,) : Rule:134
Text: (ByVal currntProcedure As String                    , Optional ByVal errorDescrption As String                    , Optional ByVal errorNumbr As GmtDateTimeErrors = -1                    )
*************
  {  -  token:2029 - (2035,) : Rule:135
Text: ByVal currntProcedure As String
*************
   {  -  token:2031 - (2031,) : Rule:139
Text: currntProcedure
*************
  {  -  token:2039 - (2047,) : Rule:135
Text: Optional ByVal errorDescrption As String
*************
   {  -  token:2043 - (2043,) : Rule:139
Text: errorDescrption
*************
  {  -  token:2051 - (2064,) : Rule:135
Text: Optional ByVal errorNumbr As GmtDateTimeErrors = -1
*************
   {  -  token:2055 - (2055,) : Rule:139
Text: errorNumbr
*************
   {  -  token:2059 - (2059,) : Rule:139
Text: GmtDateTimeErrors
DEFAULT VALUE -'' : = -1
*************
   {  -  token:2061 - (2064,) : Rule:136
Text: = -1
*************
 {  -  token:2070 - (2070,) : Rule:139
Text: mError
*************
 {  -  token:2077 - (2077,) : Rule:139
Text: HasError
*************
 {  -  token:2086 - (2086,) : Rule:139
Text: LenB
*************
 {  -  token:2088 - (2088,) : Rule:139
Text: errorDescrption
*************
 {  -  token:2097 - (2097,) : Rule:139
Text: errorDescrption
*************
 {  -  token:2102 - (2102,) : Rule:139
Text: Description
*************
 {  -  token:2106 - (2106,) : Rule:139
Text: errorDescrption
*************
 {  -  token:2111 - (2111,) : Rule:139
Text: Description
*************
 {  -  token:2115 - (2115,) : Rule:139
Text: vbCrLf
*************
 {  -  token:2119 - (2119,) : Rule:139
Text: errorDescrption
*************
 {  -  token:2124 - (2124,) : Rule:139
Text: currntProcedure
*************
 {  -  token:2132 - (2132,) : Rule:139
Text: currntProcedure
*************
 {  -  token:2141 - (2141,) : Rule:139
Text: errorNumbr
*************
 {  -  token:2150 - (2150,) : Rule:139
Text: errorNumbr
*************
 {  -  token:2155 - (2155,) : Rule:139
Text: Number
*************
 {  -  token:2162 - (2162,) : Rule:139
Text: errorNumbr
*************
 {  -  token:2166 - (2166,) : Rule:139
Text: NotInitted
*************
 {  -  token:2168 - (2168,) : Rule:139
Text: errorDescrption
*************
 {  -  token:2176 - (2176,) : Rule:139
Text: vbCrLf
*************
 {  -  token:2188 - (2188,) : Rule:139
Text: currntProcedure
*************
 {  -  token:2199 - (2199,) : Rule:139
Text: errorDescrption
*************
 {  -  token:2203 - (2203,) : Rule:139
Text: currntProcedure
*************
 {  -  token:2207 - (2207,) : Rule:139
Text: vbCrLf
*************
 {  -  token:2211 - (2211,) : Rule:139
Text: errorDescrption
*************
 {  -  token:2218 - (2218,) : Rule:139
Text: errorDescrption
*************
 {  -  token:2221 - (2221,) : Rule:139
Text: errorNumbr
*************
 {  -  token:2225 - (2225,) : Rule:139
Text: Source
{'root': {'args': {'currntProcedure': {'has_default': False,
                                       'name': 'currntProcedure',
                                       'scope': ''},
                   'dwReserved': {'has_default': False,
                                  'name': 'dwReserved',
                                  'scope': ''},
                   'errCondition': {'has_default': False,
                                    'name': 'errCondition',
                                    'scope': ''},
                   'errSource': {'has_default': False,
                                 'name': 'errSource',
                                 'scope': ''},
                   'errorDescrption': {'has_default': False,
                                       'name': 'errorDescrption',
                                       'scope': ''},
                   'errorMsg': {'has_default': False,
                                'name': 'errorMsg',
                                'scope': ''},
                   'errorNumbr': {'has_default': False,
                                  'name': 'errorNumbr',
                                  'scope': ''},
                   'lpTimeZoneInformation': {'has_default': False,
                                             'name': 'lpTimeZoneInformation',
                                             'scope': ''},
                   'lpszTime': {'has_default': False,
                                'name': 'lpszTime',
                                'scope': ''},
                   'pst': {'has_default': False, 'name': 'pst', 'scope': ''}},
          'func': {'GmtDate': {'args': {'startngDate': {'has_default': False,
                                                        'name': 'startngDate',
                                                        'scope': 'GmtDate'}},
                               'col': None,
                               'end': None,
                               'name': 'GmtDate',
                               'start': None},
                   'GmtDateLocal': {'args': {'gmtRefernceDate': {'has_default': False,
                                                                 'name': 'gmtRefernceDate',
                                                                 'scope': 'GmtDateLocal'}},
                                    'col': None,
                                    'end': None,
                                    'name': 'GmtDateLocal',
                                    'start': None},
                   'GmtFormat': {'args': {'dateFormt': {'has_default': False,
                                                        'name': 'dateFormt',
                                                        'scope': 'GmtFormat'},
                                          'dateObj': {'has_default': False,
                                                      'name': 'dateObj',
                                                      'scope': 'GmtFormat'},
                                          'gmtSuffx': {'has_default': False,
                                                       'name': 'gmtSuffx',
                                                       'scope': 'GmtFormat'}},
                                 'col': None,
                                 'end': None,
                                 'name': 'GmtFormat',
                                 'start': None},
                   'GmtStringToDate': {'args': {'internetDateStr': {'has_default': False,
                                                                    'name': 'internetDateStr',
                                                                    'scope': 'GmtStringToDate'}},
                                       'col': None,
                                       'end': None,
                                       'name': 'GmtStringToDate',
                                       'start': None},
                   'GmtTimeDifference': {'col': None,
                                         'end': None,
                                         'name': 'GmtTimeDifference',
                                         'start': None},
                   'Iso8601TimeToLocalVbTime': {'args': {'sIso8601': {'has_default': False,
                                                                      'name': 'sIso8601',
                                                                      'scope': 'Iso8601TimeToLocalVbTime'}},
                                                'col': None,
                                                'end': None,
                                                'name': 'Iso8601TimeToLocalVbTime',
                                                'start': None},
                   'Rfc822TimeToLocalVbTime': {'args': {'sRfc822': {'has_default': False,
                                                                    'name': 'sRfc822',
                                                                    'scope': 'Rfc822TimeToLocalVbTime'}},
                                               'col': None,
                                               'end': None,
                                               'name': 'Rfc822TimeToLocalVbTime',
                                               'start': None}}}}
