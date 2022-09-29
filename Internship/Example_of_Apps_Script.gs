function sendMailEdit(e){
  if (e.range.columnStart != 12 || e.value != "Approved") return;
  const rData = e.source.getActiveSheet().getRange(e.range.rowStart,1,1,11).getValues();
  let n = rData[0][3];
  let d = new Date(rData[0][0]).toLocaleDateString("en-US");
  let now = new Date().toLocaleString("en-US");
  let gender = rData[0][2];
  let filename = rData[0][9];
  let semester = rData[0][7];
  let email = rData[0][1];
  var file = DriveApp.getFilesByName(filename);
  let msg = "Attendance Letter for "+ gender +" " + n + " (" + d + ") for Semester " + semester + " Approved at " + now;
  Logger.log(msg);
  GmailApp.sendEmail(email, "Attendance Letter", msg , {attachments:[file.next().getAs(MimeType.PDF)]})
}
