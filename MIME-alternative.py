import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "********************@gmail.com" #sender
you = "*****************" #recipient

#paste your email password as we are using gmail we have to turn on the "Allow less secure apps" from "Less secure app access" from our gmail account.
#otherwise your program will unbale to login
pwd = '*****' # type password here

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "alternative"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       <b>How are you?</b><br>
       Here is the <a href="https://www.python.org">link</a> you wanted.
    </p>
    <div align="center">
		<table border="0" cellspacing="0" cellpadding="0" style="max-width:6.25in;background:white;border-collapse:collapse">
		<tbody>
		<tr>
		<td width="33%" style="width:33.32%;padding:15.0pt 0in 7.5pt 0in">
		<p class="MsoNormal"><a href="https://kbbm6lps.r.us-west-2.awstrack.me/L0/https:%2F%2Fwww.xiqinc.com%2F/1/0101016d68ab2c22-9fe2b45f-3943-452f-922c-118869233441-000000/mrQDW4TDCxkh-dChXN9uFjM7ng0=129" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://kbbm6lps.r.us-west-2.awstrack.me/L0/https:%252F%252Fwww.xiqinc.com%252F/1/0101016d68ab2c22-9fe2b45f-3943-452f-922c-118869233441-000000/mrQDW4TDCxkh-dChXN9uFjM7ng0%3D129&amp;source=gmail&amp;ust=1569571693236000&amp;usg=AFQjCNHgdO8pgNuR8R8HD-QSG5O0IDlFpg"><span style="font-family:&quot;Arial&quot;,sans-serif;text-decoration:none"><img border="0" width="102" height="27" style="width:1.0583in;height:.2833in" id="m_-5843714398106421227_x0000_i1069" src="https://ci6.googleusercontent.com/proxy/qP2HaWVr5gSYqCHe5FrxH5vRqIF21KbNUBFmUbu1sr5sSuiemh4QXj2mr0Li8YIzgqMR0QVFygfImtag46da0Go1wNJh3FW_FmijDTZTD9Rw2qfLwXXuvPq7BibDVNg_jvzpc0biaQ=s0-d-e1-ft#https://media.xiq.io/user_images/1562841948_0b800b02-a3c9-11e9-ab34-06b5fc41d42e.png" alt="xiq" class="CToWUd"></span></a><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		</td>
		<td width="33%" style="width:33.32%;padding:15.0pt 0in 0in 0in">
		<p class="MsoNormal" align="right" style="text-align:right"><span style="font-size:10.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#93a4ba;text-transform:uppercase;letter-spacing:-.5pt">Wednesday, 25 September 2019</span><span style="font-family:&quot;Arial&quot;,sans-serif">
		<u></u><u></u></span></p>
		</td>
		</tr>
		<tr>
		<td colspan="2" valign="top" style="padding:0in 0in 18.75pt 0in">
		<div align="center">
		<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr>
		<td width="50%" style="width:50.0%;background:black;padding:3.0pt 3.0pt 3.0pt 3.0pt">
		<p class="MsoNormal" align="center" style="text-align:center"><span class="m_-5843714398106421227company"><span style="font-size:8.5pt;color:white;background:black">Alibaba Group Holding Limited
		</span></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		</td>
		<td width="50%" style="width:50.0%;background:#68b828;padding:3.0pt 3.0pt 3.0pt 3.0pt">
		<p class="MsoNormal" align="center" style="text-align:center"><span class="m_-5843714398106421227category"><span style="font-size:8.5pt;color:white;background:#68b828">Earnings
		</span></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		</div>
		<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif"><img border="0" width="600" height="310" style="width:6.25in;height:3.225in" id="m_-5843714398106421227_x0000_i1068" src="https://ci6.googleusercontent.com/proxy/qSkJzfb6V4i_Zz7otq-t3zLJCKToPAez5v_Vrs4k08LxRgxKhJL4dHhxM9Y-wxVAVcVCtWNSH9QOH-BRAfEZx5l9wS-TjInD7axUrQc5HC4O2u84Mo7urBP98QgKTBw68iyLAdELO70VKLFwxlC4qY9uPIEGy8GhDQWXXukjID6qiD9AM2fCXZqKcjYZsnnRDvPHsphxbI-icw=s0-d-e1-ft#http://image.xiq.io/returnimage/?url=https://images.barrons.com/im-110321?width=1260&amp;size=1.5&amp;width=600&amp;height=310&amp;articleid=312615594" alt="Article Heading" class="CToWUd a6T" tabindex="0"><div class="a6S" dir="ltr" style="opacity: 0.01; left: 671px; top: 538.328px;"><div id=":1v1" class="T-I J-J5-Ji aQv T-I-ax7 L3 a5q" role="button" tabindex="0" aria-label="Download attachment " data-tooltip-class="a1V" data-tooltip="Download"><div class="aSK J-J5-Ji aYr"></div></div></div></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;border-collapse:collapse">
		<tbody>
		<tr>
		<td style="padding:5.25pt 0in 0in 0in">
		<p class="MsoNormal"><b><span style="font-size:15.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#30374e">Alibaba Aims to Serve 1 Billion Customers a Year by 2024</span></b><b><span style="font-size:15.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#222222">
		<u></u><u></u></span></b></p>
		</td>
		</tr>
		<tr>
		<td valign="top" style="padding:3.75pt 0in 3.75pt 0in">
		<p class="m_-5843714398106421227description" style="margin-bottom:11.25pt;line-height:12.75pt"><span style="font-size:10.5pt;color:#797e81">Alibaba management maintained its revenue guidance of 500 billion yuan for fiscal 2020. The companys near-term goal is to increase annual active
		 consumers from the current 730 million to over one billion in the next five years and nearly double its annual gross merchandise volume from 5.7 trillion yuan in fiscal 2019 to over 10 trillion yuan by 2024. Over the long term, Alibaba (ticker: BABA) wants
		 to reach ...</span><a href="http://xiqinc.app.link/?entity=article&amp;source=diq-b25bd71207c44c55bda29d063ac86bb5&amp;id=312615594&amp;url=https://www.barrons.com/articles/alibaba-aims-to-serve-1-billion-customers-a-year-by-2024-51569349858" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://xiqinc.app.link/?entity%3Darticle%26source%3Ddiq-b25bd71207c44c55bda29d063ac86bb5%26id%3D312615594%26url%3Dhttps://www.barrons.com/articles/alibaba-aims-to-serve-1-billion-customers-a-year-by-2024-51569349858&amp;source=gmail&amp;ust=1569571693236000&amp;usg=AFQjCNGfybpzWHlYA93gEGKalfbztmJ8MA"><b><span style="font-size:10.5pt;color:#9013fe">READ
		 MORE</span></b></a><span style="font-size:10.5pt;color:#797e81"> <u></u><u></u></span></p>
		<p class="m_-5843714398106421227time-company" style="line-height:11.25pt"><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">SEP 24, 2019
		</span><span class="m_-5843714398106421227tag-space"><span style="font-size:9.0pt;color:white;letter-spacing:-.25pt;background:white">. . .</span></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt"> |
		</span><span class="m_-5843714398106421227tag-space"><span style="font-size:9.0pt;color:white;letter-spacing:-.25pt;background:white">. . .</span></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">
		</span><span style="font-size:9.0pt;color:#45b5eb;letter-spacing:-.25pt"><a href="http://barrons.com" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://barrons.com&amp;source=gmail&amp;ust=1569571693236000&amp;usg=AFQjCNE9bjJPKCsyVvHdYbTlBQNbqwRYcQ">barrons.com</a></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">
		<u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		</td>
		</tr>
		<tr>
		<td width="50%" valign="top" style="width:50.0%;padding:0in 6.0pt 0in 0in">
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr style="height:272.25pt">
		<td valign="top" style="border:solid #cfdae8 1.0pt;padding:7.5pt 11.25pt 7.5pt 11.25pt;height:272.25pt">
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr>
		<td style="border:none;border-bottom:solid #cfdae8 1.0pt;padding:3.75pt 0in 7.5pt 0in">
		<p class="MsoNormal"><b><span style="font-family:&quot;Arial&quot;,sans-serif"><img border="0" width="31" height="16" style="width:.325in;height:.1666in" id="m_-5843714398106421227_x0000_i1067" src="https://ci5.googleusercontent.com/proxy/eccw9D_m1___R3eTpcY09b5DonUTXzCbjkqbLpoWY4uVtnUn052yObvaihTw9Rpl49X1pgz6llYFC7oM-irsCE-pOCD61UnVLam6hEaQqD7vmzBUeERDV_faiG8OzArSmsrCB9bJ5g=s0-d-e1-ft#https://media.xiq.io/user_images/1561548164_b7c7ffd0-9804-11e9-8f23-06b5fc41d42e.png" alt="https://media.xiq.io/user_images/1561548164_b7c7ffd0-9804-11e9-8f23-06b5fc41d42e.png" class="CToWUd"></span></b><b><span style="font-size:15.0pt;font-family:&quot;Arial&quot;,sans-serif;color:white">.</span></b><span class="m_-5843714398106421227pulse-title"><b><span style="font-size:15.0pt;color:black">PULSE</span></b></span><b><span style="font-family:&quot;Arial&quot;,sans-serif">
		<u></u><u></u></span></b></p>
		</td>
		</tr>
		</tbody>
		</table>
		<div>
		<div id="m_-5843714398106421227myTabContent">
		<div id="m_-5843714398106421227home">
		<div>
		<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif;display:none"><u></u>&nbsp;<u></u></span></p>
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr style="height:6.75pt">
		<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:6.75pt">
		<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="9" style="width:1.0416in;height:.0916in" id="m_-5843714398106421227_x0000_i1066" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" class="CToWUd"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr>
		<td style="padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span class="m_-5843714398106421227text"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">Apple, Inc.</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
		<span class="m_-5843714398106421227count">(15)</span> <span class="m_-5843714398106421227angle-right">&nbsp;</span></span></b><span class="m_-5843714398106421227angle-right"><b><span style="font-size:7.5pt;font-family:&quot;Cambria Math&quot;,serif;color:#001760;text-transform:uppercase">〉</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
		</span></b><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr style="height:2.25pt">
		<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:2.25pt">
		<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="3" style="width:1.0416in;height:.0333in" id="m_-5843714398106421227_x0000_i1065" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" class="CToWUd"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif;display:none"><u></u>&nbsp;<u></u></span></p>
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr>
		<td width="0%" style="width:0%;background:#5ca323;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#5ca323">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#5ca323"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#d64025;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#d64025">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#d64025"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#ff484b;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#ff484b">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#ff484b"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#40bbea;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#40bbea">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#40bbea"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#301220;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#301220">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#301220"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#68b828;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#68b828">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#68b828"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#009f79;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#009f79">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#009f79"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#f69f2f;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#f69f2f">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#f69f2f"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#701e41;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#701e41">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#701e41"><u></u><u></u></span></p>
		</td>
		<td width="6%" style="width:6.66%;background:#00b19d;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#00b19d">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#00b19d"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#8dc63f;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#8dc63f">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#8dc63f"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#7c38bc;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#7c38bc">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#7c38bc"><u></u><u></u></span></p>
		</td>
		<td width="6%" style="width:6.66%;background:#cc3f44;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#cc3f44">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#cc3f44"><u></u><u></u></span></p>
		</td>
		<td width="66%" style="width:66.62%;background:#0e62c7;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#0e62c7">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#0e62c7"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#ffba00;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#ffba00">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#ffba00"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#a3a375;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#a3a375">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#a3a375"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#75a3a3;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#75a3a3">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#75a3a3"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#4483ea;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#4483ea">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#4483ea"><u></u><u></u></span></p>
		</td>
		<td width="20%" style="width:20.0%;background:#84d2c7;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#84d2c7">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#84d2c7"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		</div>
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr style="height:6.75pt">
		<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:6.75pt">
		<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="9" style="width:1.0416in;height:.0916in" id="m_-5843714398106421227_x0000_i1064" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" class="CToWUd"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr>
		<td style="padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span class="m_-5843714398106421227text"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">Google Inc.</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
		<span class="m_-5843714398106421227count">(12)</span> <span class="m_-5843714398106421227angle-right">&nbsp;</span></span></b><span class="m_-5843714398106421227angle-right"><b><span style="font-size:7.5pt;font-family:&quot;Cambria Math&quot;,serif;color:#001760;text-transform:uppercase">〉</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
		</span></b><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr style="height:2.25pt">
		<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:2.25pt">
		<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="3" style="width:1.0416in;height:.0333in" id="m_-5843714398106421227_x0000_i1063" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" class="CToWUd"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif;display:none"><u></u>&nbsp;<u></u></span></p>
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr>
		<td width="0%" style="width:0%;background:#5ca323;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#5ca323">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#5ca323"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#d64025;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#d64025">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#d64025"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#ff484b;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#ff484b">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#ff484b"><u></u><u></u></span></p>
		</td>
		<td width="8%" style="width:8.32%;background:#40bbea;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#40bbea">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#40bbea"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#301220;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#301220">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#301220"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#68b828;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#68b828">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#68b828"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#009f79;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#009f79">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#009f79"><u></u><u></u></span></p>
		</td>
		<td width="25%" style="width:25.0%;background:#f69f2f;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#f69f2f">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#f69f2f"><u></u><u></u></span></p>
		</td>
		<td width="16%" style="width:16.66%;background:#701e41;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#701e41">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#701e41"><u></u><u></u></span></p>
		</td>
		<td width="8%" style="width:8.32%;background:#00b19d;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#00b19d">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#00b19d"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#8dc63f;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#8dc63f">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#8dc63f"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#7c38bc;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#7c38bc">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#7c38bc"><u></u><u></u></span></p>
		</td>
		<td width="16%" style="width:16.66%;background:#cc3f44;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#cc3f44">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#cc3f44"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#0e62c7;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#0e62c7">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#0e62c7"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#ffba00;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#ffba00">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#ffba00"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#a3a375;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#a3a375">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#a3a375"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#75a3a3;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#75a3a3">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#75a3a3"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#4483ea;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#4483ea">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#4483ea"><u></u><u></u></span></p>
		</td>
		<td width="25%" style="width:25.0%;background:#84d2c7;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#84d2c7">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#84d2c7"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		<div>
		<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif;display:none"><u></u>&nbsp;<u></u></span></p>
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr style="height:6.75pt">
		<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:6.75pt">
		<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="9" style="width:1.0416in;height:.0916in" id="m_-5843714398106421227_x0000_i1062" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" class="CToWUd"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr>
		<td style="padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span class="m_-5843714398106421227text"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">Accenture plc
		</span></b></span><span class="m_-5843714398106421227count"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">(8)</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
		<span class="m_-5843714398106421227angle-right">&nbsp;</span></span></b><span class="m_-5843714398106421227angle-right"><b><span style="font-size:7.5pt;font-family:&quot;Cambria Math&quot;,serif;color:#001760;text-transform:uppercase">〉</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
		</span></b><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr style="height:2.25pt">
		<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:2.25pt">
		<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="3" style="width:1.0416in;height:.0333in" id="m_-5843714398106421227_x0000_i1061" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" class="CToWUd"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif;display:none"><u></u>&nbsp;<u></u></span></p>
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr>
		<td width="12%" style="width:12.5%;background:#5ca323;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#5ca323">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#5ca323"><u></u><u></u></span></p>
		</td>
		<td width="12%" style="width:12.5%;background:#d64025;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#d64025">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#d64025"><u></u><u></u></span></p>
		</td>
		<td width="12%" style="width:12.5%;background:#ff484b;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#ff484b">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#ff484b"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#40bbea;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#40bbea">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#40bbea"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#301220;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#301220">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#301220"><u></u><u></u></span></p>
		</td>
		<td width="12%" style="width:12.5%;background:#68b828;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#68b828">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#68b828"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#009f79;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#009f79">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#009f79"><u></u><u></u></span></p>
		</td>
		<td width="25%" style="width:25.0%;background:#f69f2f;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#f69f2f">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#f69f2f"><u></u><u></u></span></p>
		</td>
		<td width="12%" style="width:12.5%;background:#701e41;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#701e41">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#701e41"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#00b19d;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#00b19d">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#00b19d"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#8dc63f;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#8dc63f">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#8dc63f"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#7c38bc;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#7c38bc">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#7c38bc"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#cc3f44;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#cc3f44">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#cc3f44"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#0e62c7;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#0e62c7">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#0e62c7"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#ffba00;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#ffba00">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#ffba00"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#a3a375;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#a3a375">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#a3a375"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#75a3a3;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#75a3a3">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#75a3a3"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#4483ea;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#4483ea">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#4483ea"><u></u><u></u></span></p>
		</td>
		<td width="12%" style="width:12.5%;background:#84d2c7;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#84d2c7">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#84d2c7"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		</div>
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr style="height:6.75pt">
		<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:6.75pt">
		<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="9" style="width:1.0416in;height:.0916in" id="m_-5843714398106421227_x0000_i1060" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" class="CToWUd"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr>
		<td style="padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span class="m_-5843714398106421227text"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">Alibaba Group Holding Limited
		</span></b></span><span class="m_-5843714398106421227count"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">(8)</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
		<span class="m_-5843714398106421227angle-right">&nbsp;</span></span></b><span class="m_-5843714398106421227angle-right"><b><span style="font-size:7.5pt;font-family:&quot;Cambria Math&quot;,serif;color:#001760;text-transform:uppercase">〉</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
		</span></b><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr style="height:2.25pt">
		<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:2.25pt">
		<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="3" style="width:1.0416in;height:.0333in" id="m_-5843714398106421227_x0000_i1059" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" class="CToWUd"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif;display:none"><u></u>&nbsp;<u></u></span></p>
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr>
		<td width="0%" style="width:0%;background:#5ca323;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#5ca323">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#5ca323"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#d64025;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#d64025">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#d64025"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#ff484b;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#ff484b">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#ff484b"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#40bbea;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#40bbea">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#40bbea"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#301220;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#301220">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#301220"><u></u><u></u></span></p>
		</td>
		<td width="12%" style="width:12.5%;background:#68b828;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#68b828">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#68b828"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#009f79;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#009f79">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#009f79"><u></u><u></u></span></p>
		</td>
		<td width="12%" style="width:12.5%;background:#f69f2f;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#f69f2f">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#f69f2f"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#701e41;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#701e41">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#701e41"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#00b19d;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#00b19d">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#00b19d"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#8dc63f;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#8dc63f">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#8dc63f"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#7c38bc;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#7c38bc">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#7c38bc"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#cc3f44;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#cc3f44">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#cc3f44"><u></u><u></u></span></p>
		</td>
		<td width="12%" style="width:12.5%;background:#0e62c7;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#0e62c7">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#0e62c7"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#ffba00;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#ffba00">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#ffba00"><u></u><u></u></span></p>
		</td>
		<td width="12%" style="width:12.5%;background:#a3a375;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#a3a375">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#a3a375"><u></u><u></u></span></p>
		</td>
		<td width="12%" style="width:12.5%;background:#75a3a3;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#75a3a3">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#75a3a3"><u></u><u></u></span></p>
		</td>
		<td width="12%" style="width:12.5%;background:#4483ea;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#4483ea">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#4483ea"><u></u><u></u></span></p>
		</td>
		<td width="25%" style="width:25.0%;background:#84d2c7;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#84d2c7">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#84d2c7"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		<div>
		<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif;display:none"><u></u>&nbsp;<u></u></span></p>
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr style="height:6.75pt">
		<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:6.75pt">
		<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="9" style="width:1.0416in;height:.0916in" id="m_-5843714398106421227_x0000_i1058" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" class="CToWUd"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr>
		<td style="padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span class="m_-5843714398106421227text"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">Twitter, Inc.</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
		<span class="m_-5843714398106421227count">(5)</span> <span class="m_-5843714398106421227angle-right">&nbsp;</span></span></b><span class="m_-5843714398106421227angle-right"><b><span style="font-size:7.5pt;font-family:&quot;Cambria Math&quot;,serif;color:#001760;text-transform:uppercase">〉</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
		</span></b><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr style="height:2.25pt">
		<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:2.25pt">
		<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="3" style="width:1.0416in;height:.0333in" id="m_-5843714398106421227_x0000_i1057" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" class="CToWUd"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif;display:none"><u></u>&nbsp;<u></u></span></p>
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr>
		<td width="0%" style="width:0%;background:#5ca323;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#5ca323">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#5ca323"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#d64025;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#d64025">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#d64025"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#ff484b;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#ff484b">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#ff484b"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#40bbea;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#40bbea">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#40bbea"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#301220;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#301220">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#301220"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#68b828;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#68b828">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#68b828"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#009f79;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#009f79">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#009f79"><u></u><u></u></span></p>
		</td>
		<td width="60%" style="width:60.0%;background:#f69f2f;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#f69f2f">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#f69f2f"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#701e41;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#701e41">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#701e41"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#00b19d;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#00b19d">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#00b19d"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#8dc63f;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#8dc63f">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#8dc63f"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#7c38bc;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#7c38bc">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#7c38bc"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#cc3f44;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#cc3f44">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#cc3f44"><u></u><u></u></span></p>
		</td>
		<td width="40%" style="width:40.0%;background:#0e62c7;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#0e62c7">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#0e62c7"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#ffba00;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#ffba00">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#ffba00"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#a3a375;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#a3a375">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#a3a375"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#75a3a3;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#75a3a3">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#75a3a3"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#4483ea;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#4483ea">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#4483ea"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#84d2c7;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#84d2c7">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#84d2c7"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		</div>
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr style="height:6.75pt">
		<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:6.75pt">
		<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="9" style="width:1.0416in;height:.0916in" id="m_-5843714398106421227_x0000_i1056" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" class="CToWUd"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr>
		<td style="padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span class="m_-5843714398106421227text"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">Dell, Inc.</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
		<span class="m_-5843714398106421227count">(4)</span> <span class="m_-5843714398106421227angle-right">&nbsp;</span></span></b><span class="m_-5843714398106421227angle-right"><b><span style="font-size:7.5pt;font-family:&quot;Cambria Math&quot;,serif;color:#001760;text-transform:uppercase">〉</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
		</span></b><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr style="height:2.25pt">
		<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:2.25pt">
		<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="3" style="width:1.0416in;height:.0333in" id="m_-5843714398106421227_x0000_i1055" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" class="CToWUd"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif;display:none"><u></u>&nbsp;<u></u></span></p>
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr>
		<td width="0%" style="width:0%;background:#5ca323;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#5ca323">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#5ca323"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#d64025;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#d64025">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#d64025"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#ff484b;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#ff484b">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#ff484b"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#40bbea;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#40bbea">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#40bbea"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#301220;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#301220">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#301220"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#68b828;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#68b828">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#68b828"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#009f79;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#009f79">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#009f79"><u></u><u></u></span></p>
		</td>
		<td width="75%" style="width:75.0%;background:#f69f2f;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#f69f2f">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#f69f2f"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#701e41;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#701e41">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#701e41"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#00b19d;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#00b19d">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#00b19d"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#8dc63f;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#8dc63f">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#8dc63f"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#7c38bc;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#7c38bc">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#7c38bc"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#cc3f44;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#cc3f44">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#cc3f44"><u></u><u></u></span></p>
		</td>
		<td width="25%" style="width:25.0%;background:#0e62c7;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#0e62c7">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#0e62c7"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#ffba00;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#ffba00">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#ffba00"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#a3a375;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#a3a375">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#a3a375"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#75a3a3;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#75a3a3">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#75a3a3"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#4483ea;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#4483ea">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#4483ea"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#84d2c7;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#84d2c7">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#84d2c7"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		<div>
		<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif;display:none"><u></u>&nbsp;<u></u></span></p>
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr style="height:6.75pt">
		<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:6.75pt">
		<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="9" style="width:1.0416in;height:.0916in" id="m_-5843714398106421227_x0000_i1054" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" class="CToWUd"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr>
		<td style="padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span class="m_-5843714398106421227text"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">Microsoft Corporation</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
		<span class="m_-5843714398106421227count">(4)</span> <span class="m_-5843714398106421227angle-right">&nbsp;</span></span></b><span class="m_-5843714398106421227angle-right"><b><span style="font-size:7.5pt;font-family:&quot;Cambria Math&quot;,serif;color:#001760;text-transform:uppercase">〉</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
		</span></b><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr style="height:2.25pt">
		<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:2.25pt">
		<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="3" style="width:1.0416in;height:.0333in" id="m_-5843714398106421227_x0000_i1053" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" class="CToWUd"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif;display:none"><u></u>&nbsp;<u></u></span></p>
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr>
		<td width="0%" style="width:0%;background:#5ca323;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#5ca323">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#5ca323"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#d64025;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#d64025">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#d64025"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#ff484b;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#ff484b">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#ff484b"><u></u><u></u></span></p>
		</td>
		<td width="25%" style="width:25.0%;background:#40bbea;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#40bbea">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#40bbea"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#301220;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#301220">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#301220"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#68b828;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#68b828">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#68b828"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#009f79;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#009f79">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#009f79"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#f69f2f;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#f69f2f">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#f69f2f"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#701e41;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#701e41">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#701e41"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#00b19d;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#00b19d">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#00b19d"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#8dc63f;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#8dc63f">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#8dc63f"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#7c38bc;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#7c38bc">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#7c38bc"><u></u><u></u></span></p>
		</td>
		<td width="75%" style="width:75.0%;background:#cc3f44;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#cc3f44">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#cc3f44"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#0e62c7;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#0e62c7">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#0e62c7"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#ffba00;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#ffba00">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#ffba00"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#a3a375;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#a3a375">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#a3a375"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#75a3a3;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#75a3a3">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#75a3a3"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#4483ea;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#4483ea">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#4483ea"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#84d2c7;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#84d2c7">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#84d2c7"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		</div>
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr style="height:6.75pt">
		<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:6.75pt">
		<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="9" style="width:1.0416in;height:.0916in" id="m_-5843714398106421227_x0000_i1052" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" class="CToWUd"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr>
		<td style="padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span class="m_-5843714398106421227text"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">Facebook, Inc.</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
		<span class="m_-5843714398106421227count">(2)</span> <span class="m_-5843714398106421227angle-right">&nbsp;</span></span></b><span class="m_-5843714398106421227angle-right"><b><span style="font-size:7.5pt;font-family:&quot;Cambria Math&quot;,serif;color:#001760;text-transform:uppercase">〉</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
		</span></b><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr style="height:2.25pt">
		<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:2.25pt">
		<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="3" style="width:1.0416in;height:.0333in" id="m_-5843714398106421227_x0000_i1051" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" class="CToWUd"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif;display:none"><u></u>&nbsp;<u></u></span></p>
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr>
		<td width="0%" style="width:0%;background:#5ca323;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#5ca323">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#5ca323"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#d64025;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#d64025">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#d64025"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#ff484b;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#ff484b">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#ff484b"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#40bbea;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#40bbea">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#40bbea"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#301220;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#301220">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#301220"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#68b828;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#68b828">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#68b828"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#009f79;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#009f79">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#009f79"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#f69f2f;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#f69f2f">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#f69f2f"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#701e41;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#701e41">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#701e41"><u></u><u></u></span></p>
		</td>
		<td width="50%" style="width:50.0%;background:#00b19d;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#00b19d">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#00b19d"><u></u><u></u></span></p>
		</td>
		<td width="50%" style="width:50.0%;background:#8dc63f;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#8dc63f">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#8dc63f"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#7c38bc;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#7c38bc">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#7c38bc"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#cc3f44;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#cc3f44">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#cc3f44"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#0e62c7;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#0e62c7">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#0e62c7"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#ffba00;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#ffba00">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#ffba00"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#a3a375;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#a3a375">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#a3a375"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#75a3a3;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#75a3a3">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#75a3a3"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#4483ea;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#4483ea">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#4483ea"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#84d2c7;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#84d2c7">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#84d2c7"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		<div>
		<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif;display:none"><u></u>&nbsp;<u></u></span></p>
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr style="height:6.75pt">
		<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:6.75pt">
		<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="9" style="width:1.0416in;height:.0916in" id="m_-5843714398106421227_x0000_i1050" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" class="CToWUd"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr>
		<td style="padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span class="m_-5843714398106421227text"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">Genpact Ltd.
		</span></b></span><span class="m_-5843714398106421227count"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">(2)</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
		<span class="m_-5843714398106421227angle-right">&nbsp;</span></span></b><span class="m_-5843714398106421227angle-right"><b><span style="font-size:7.5pt;font-family:&quot;Cambria Math&quot;,serif;color:#001760;text-transform:uppercase">〉</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
		</span></b><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr style="height:2.25pt">
		<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:2.25pt">
		<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="3" style="width:1.0416in;height:.0333in" id="m_-5843714398106421227_x0000_i1049" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" class="CToWUd"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif;display:none"><u></u>&nbsp;<u></u></span></p>
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr>
		<td width="0%" style="width:0%;background:#5ca323;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#5ca323">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#5ca323"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#d64025;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#d64025">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#d64025"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#ff484b;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#ff484b">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#ff484b"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#40bbea;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#40bbea">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#40bbea"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#301220;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#301220">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#301220"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#68b828;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#68b828">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#68b828"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#009f79;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#009f79">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#009f79"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#f69f2f;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#f69f2f">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#f69f2f"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#701e41;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#701e41">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#701e41"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#00b19d;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#00b19d">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#00b19d"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#8dc63f;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#8dc63f">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#8dc63f"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#7c38bc;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#7c38bc">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#7c38bc"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#cc3f44;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#cc3f44">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#cc3f44"><u></u><u></u></span></p>
		</td>
		<td width="50%" style="width:50.0%;background:#0e62c7;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#0e62c7">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#0e62c7"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#ffba00;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#ffba00">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#ffba00"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#a3a375;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#a3a375">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#a3a375"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#75a3a3;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#75a3a3">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#75a3a3"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#4483ea;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#4483ea">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#4483ea"><u></u><u></u></span></p>
		</td>
		<td width="50%" style="width:50.0%;background:#84d2c7;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#84d2c7">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#84d2c7"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		</div>
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr style="height:6.75pt">
		<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:6.75pt">
		<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="9" style="width:1.0416in;height:.0916in" id="m_-5843714398106421227_x0000_i1048" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" class="CToWUd"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr>
		<td style="padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span class="m_-5843714398106421227text"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">Oracle Corp</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
		<span class="m_-5843714398106421227count">(2)</span> <span class="m_-5843714398106421227angle-right">&nbsp;</span></span></b><span class="m_-5843714398106421227angle-right"><b><span style="font-size:7.5pt;font-family:&quot;Cambria Math&quot;,serif;color:#001760;text-transform:uppercase">〉</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
		</span></b><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr style="height:2.25pt">
		<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:2.25pt">
		<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="3" style="width:1.0416in;height:.0333in" id="m_-5843714398106421227_x0000_i1047" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" class="CToWUd"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif;display:none"><u></u>&nbsp;<u></u></span></p>
		<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr>
		<td width="0%" style="width:0%;background:#5ca323;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#5ca323">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#5ca323"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#d64025;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#d64025">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#d64025"><u></u><u></u></span></p>
		</td>
		<td width="50%" style="width:50.0%;background:#ff484b;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#ff484b">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#ff484b"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#40bbea;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#40bbea">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#40bbea"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#301220;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#301220">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#301220"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#68b828;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#68b828">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#68b828"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#009f79;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#009f79">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#009f79"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#f69f2f;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#f69f2f">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#f69f2f"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#701e41;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#701e41">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#701e41"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#00b19d;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#00b19d">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#00b19d"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#8dc63f;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#8dc63f">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#8dc63f"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#7c38bc;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#7c38bc">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#7c38bc"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#cc3f44;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#cc3f44">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#cc3f44"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#0e62c7;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#0e62c7">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#0e62c7"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#ffba00;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#ffba00">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#ffba00"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#a3a375;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#a3a375">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#a3a375"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#75a3a3;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#75a3a3">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#75a3a3"><u></u><u></u></span></p>
		</td>
		<td width="50%" style="width:50.0%;background:#4483ea;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#4483ea">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#4483ea"><u></u><u></u></span></p>
		</td>
		<td width="0%" style="width:0%;background:#84d2c7;padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-size:6.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#84d2c7">.</span><span style="font-family:&quot;Arial&quot;,sans-serif;color:#84d2c7"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		</div>
		</div>
		</div>
		<p class="MsoNormal"><u></u><u></u></p>
		</td>
		</tr>
		</tbody>
		</table>
		</td>
		<td width="50%" valign="top" style="width:50.0%;padding:0in 0in 0in 6.0pt">
		<div align="center">
		<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr>
		<td width="50%" style="width:50.0%;background:black;padding:3.0pt 3.0pt 3.0pt 3.0pt">
		<p class="MsoNormal" align="center" style="text-align:center"><span class="m_-5843714398106421227company"><span style="font-size:8.5pt;color:white;background:black">Accenture plc
		</span></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		</td>
		<td width="50%" style="width:50.0%;background:#d64025;padding:3.0pt 3.0pt 3.0pt 3.0pt">
		<p class="MsoNormal" align="center" style="text-align:center"><span class="m_-5843714398106421227category"><span style="font-size:8.5pt;color:white;background:#d64025">CxO Moves
		</span></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		</div>
		<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif"><img border="0" width="292" height="192" style="width:3.0416in;height:2.0in" id="m_-5843714398106421227_x0000_i1046" src="https://ci4.googleusercontent.com/proxy/aVvPDxKLKaV1_4fb0YyQe98ryFQ8twXR6lAiMLD6wQcRNdu1PxuRSQuSie9s8_Ww6x-pHGia9OZLBTlE7AimC0JKRc58-YFviA8cF93uWaj-QiSlAcbMHvCOqYc2QggkAd4ORXlVajRJSoE_wT28cSt4_gTXyhCwN7snWuZpNAuTChotiMWpV2rSM1c3zbtNpJ8nSCjrVxVn-Hre2NP64WTAaYuyJXwghh6aDTyoOtZU4Apu2DT5TZgzIePxbN9KKjRJI42HP7eC6kUySqfsQiPly4ekoI-B=s0-d-e1-ft#http://image.xiq.io/returnimage/?url=http://ec2-54-200-50-167.us-west-2.compute.amazonaws.com/static/admin/upload/542b85b2-df14-11e9-a117-06945eaf9ebf.jpeg&amp;width=292&amp;height=192&amp;articleid=312579976" alt="Article Heading" class="CToWUd"></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;border-collapse:collapse">
		<tbody>
		<tr>
		<td style="padding:5.25pt 0in 0in 0in">
		<p class="MsoNormal"><b><span style="font-size:15.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#30374e">Accenture Names Simon Eaves Group Chief Executive Products, ...</span></b><b><span style="font-size:15.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#222222">
		<u></u><u></u></span></b></p>
		</td>
		</tr>
		<tr>
		<td valign="top" style="padding:3.75pt 0in 3.75pt 0in">
		<p class="m_-5843714398106421227description" style="margin-bottom:11.25pt;line-height:12.75pt"><span style="font-size:10.5pt;color:#797e81">NEW YORK; Sept. 24, 2019 Accenture (NYSE: ACN) has appointed Simon Eaves as group chief executive ...
		</span><a href="http://xiqinc.app.link/?entity=article&amp;source=diq-b25bd71207c44c55bda29d063ac86bb5&amp;id=312579976&amp;url=https://newsroom.accenture.com/news/accenture-names-simon-eaves-group-chief-executive-products-succeeding-sander-van-t-noordende.htm" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://xiqinc.app.link/?entity%3Darticle%26source%3Ddiq-b25bd71207c44c55bda29d063ac86bb5%26id%3D312579976%26url%3Dhttps://newsroom.accenture.com/news/accenture-names-simon-eaves-group-chief-executive-products-succeeding-sander-van-t-noordende.htm&amp;source=gmail&amp;ust=1569571693241000&amp;usg=AFQjCNFW1OJAz4siPrtEQ1eea6CJJhBLaw"><b><span style="font-size:10.5pt;color:#9013fe">READ
		 MORE</span></b></a><span style="font-size:10.5pt;color:#797e81"> <u></u><u></u></span></p>
		<p class="m_-5843714398106421227time-company" style="line-height:11.25pt"><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">SEP 24, 2019
		</span><span class="m_-5843714398106421227tag-space"><span style="font-size:9.0pt;color:white;letter-spacing:-.25pt;background:white">. . .</span></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt"> |
		</span><span class="m_-5843714398106421227tag-space"><span style="font-size:9.0pt;color:white;letter-spacing:-.25pt;background:white">. . .</span></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">
		</span><span style="font-size:9.0pt;color:#45b5eb;letter-spacing:-.25pt"><a href="http://newsroom.accenture.com" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://newsroom.accenture.com&amp;source=gmail&amp;ust=1569571693241000&amp;usg=AFQjCNH61Fwubwa-SeZollnK55-jopT3VA">newsroom.accenture.com</a></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">
		<u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		</td>
		</tr>
		<tr>
		<td colspan="2" style="padding:0in 0in 0in 0in">
		<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif"><img border="0" width="600" height="62" style="width:6.25in;height:.6416in" id="m_-5843714398106421227_x0000_i1045" src="https://ci4.googleusercontent.com/proxy/ZvYaY0nzldgo9E9Q5P3M7O3PSyZ5I2BS83qxTsvS9QmG6y73YhQ0TLWGEy8hUWmbPOLrWqaTIJHyFjboZ2KLY3XpyoZHj5q7T9yDgwuK2TXZxwD4CfUHTDr1ZOIH6581wYxWKWxhSg=s0-d-e1-ft#https://media.xiq.io/user_images/1563360050_58120730-a87f-11e9-94d5-06b5fc41d42e.png" alt="https://media.xiq.io/user_images/1563360050_58120730-a87f-11e9-94d5-06b5fc41d42e.png" class="CToWUd"></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		</td>
		</tr>
		<tr>
		<td colspan="2" valign="top" style="padding:0in 0in 18.75pt 0in">
		<div align="center">
		<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr>
		<td width="50%" style="width:50.0%;background:black;padding:3.0pt 3.0pt 3.0pt 3.0pt">
		<p class="MsoNormal" align="center" style="text-align:center"><span class="m_-5843714398106421227company"><span style="font-size:8.5pt;color:white;background:black">Facebook, Inc.
		</span></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		</td>
		<td width="50%" style="width:50.0%;background:#8dc63f;padding:3.0pt 3.0pt 3.0pt 3.0pt">
		<p class="MsoNormal" align="center" style="text-align:center"><span class="m_-5843714398106421227category"><span style="font-size:8.5pt;color:white;background:#8dc63f">M&amp;A
		</span></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		</div>
		<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif"><img border="0" width="600" height="310" style="width:6.25in;height:3.225in" id="m_-5843714398106421227_x0000_i1044" src="https://ci5.googleusercontent.com/proxy/w9L7lTTneWyk5zd3V6ma2YP58uvv3SS-lil0wXtVAy1Q5wh9XH34sspztxKEqOqBhSPtBYJsDkT43MDIZsb1xcNvh2eqf56Gg07nJMda15uyBHCkgcqiFodyMuobECapHeHm0TLsko6i6b-EdmVW50PLJiMvYF0TG8gp3IKzmxIzHydbz3H0W7bfNyhcuDuN23ldJRr3OtVQvQQqYd4SCH3JosJkcCkVnJsut7fJZHPztzSCyYfSKE5zupKHxT0JjDIS=s0-d-e1-ft#http://image.xiq.io/returnimage/?url=https://content.fortune.com/wp-content/uploads/2019/09/GettyImages-1170810085.jpg?resize=1200,600&amp;width=600&amp;height=310&amp;articleid=312621537" alt="Article Heading" class="CToWUd a6T" tabindex="0"><div class="a6S" dir="ltr" style="opacity: 0.01; left: 671px; top: 1964.33px;"><div id=":1v2" class="T-I J-J5-Ji aQv T-I-ax7 L3 a5q" title="Download" role="button" tabindex="0" aria-label="Download attachment " data-tooltip-class="a1V"><div class="aSK J-J5-Ji aYr"></div></div></div></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;border-collapse:collapse">
		<tbody>
		<tr>
		<td style="padding:5.25pt 0in 0in 0in">
		<p class="MsoNormal"><b><span style="font-size:15.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#30374e">Why Facebooks CTRL-Labs Buy Could Be a Red Flag for the FTC</span></b><b><span style="font-size:15.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#222222">
		<u></u><u></u></span></b></p>
		</td>
		</tr>
		<tr>
		<td valign="top" style="padding:3.75pt 0in 3.75pt 0in">
		<p class="m_-5843714398106421227description" style="margin-bottom:11.25pt;line-height:12.75pt"><span style="font-size:10.5pt;color:#797e81">Facebook Inc. sent a clear signal with its agreement to buy a brain computing startup: heightened regulatory scrutiny and intensifying antitrust
		 probes wont slow down its pace of acquisitions. With its announcement Monday of plans to purchase CTRL-Labs for at least $500 million, Facebook continued its pattern ...</span><a href="http://xiqinc.app.link/?entity=article&amp;source=diq-b25bd71207c44c55bda29d063ac86bb5&amp;id=312621537&amp;url=https://fortune.com/2019/09/25/facebook-ctrl-labs-ftc-antitrust/" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://xiqinc.app.link/?entity%3Darticle%26source%3Ddiq-b25bd71207c44c55bda29d063ac86bb5%26id%3D312621537%26url%3Dhttps://fortune.com/2019/09/25/facebook-ctrl-labs-ftc-antitrust/&amp;source=gmail&amp;ust=1569571693242000&amp;usg=AFQjCNHoOHMfM_XrcP8zZ5j9MmcGvhB-Gw"><b><span style="font-size:10.5pt;color:#9013fe">READ
		 MORE</span></b></a><span style="font-size:10.5pt;color:#797e81"> <u></u><u></u></span></p>
		<p class="m_-5843714398106421227time-company" style="line-height:11.25pt"><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">SEP 25, 2019
		</span><span class="m_-5843714398106421227tag-space"><span style="font-size:9.0pt;color:white;letter-spacing:-.25pt;background:white">. . .</span></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt"> |
		</span><span class="m_-5843714398106421227tag-space"><span style="font-size:9.0pt;color:white;letter-spacing:-.25pt;background:white">. . .</span></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">
		</span><span style="font-size:9.0pt;color:#45b5eb;letter-spacing:-.25pt"><a href="http://fortune.com" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://fortune.com&amp;source=gmail&amp;ust=1569571693242000&amp;usg=AFQjCNE65uKFqHR0fTOaFV9yrGNcEnjENg">fortune.com</a></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">
		<u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		</td>
		</tr>
		<tr>
		<td width="50%" valign="top" style="width:50.0%;padding:0in 6.0pt 18.75pt 0in">
		<div align="center">
		<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
		<tbody>
		<tr>
		<td width="50%" style="width:50.0%;background:black;padding:3.0pt 3.0pt 3.0pt 3.0pt">
		<p class="MsoNormal" align="center" style="text-align:center"><span class="m_-5843714398106421227company"><span style="font-size:8.5pt;color:white;background:black">Oracle Corp
		</span></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		</td>
		<td width="50%" style="width:50.0%;background:#ff484b;padding:3.0pt 3.0pt 3.0pt 3.0pt">
		<p class="MsoNormal" align="center" style="text-align:center"><span class="m_-5843714398106421227category"><span style="font-size:8.5pt;color:white;background:#ff484b">CxO News
		</span></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		</td>
		</tr>
		</tbody>
		</table>
		</div>
		<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif"><img border="0" width="292" height="192" style="width:3.0416in;height:2.0in" id="m_-5843714398106421227_x0000_i1043" src="https://ci3.googleusercontent.com/proxy/6uA4oilYtmgPDzC5bwvtf28bGwyz7-ES90li0H64gX5S6w4ePslNQNTk87HzO0KrVE6CEkmtI3RT0cQNwU1yGzxADkO8zXTmxA3fbg70T481J9d1M1hXotuZ5khD_E79ohz29--iDAjwiTnaK38RSF6E-oPWyoFBMuiBbuk644-9CoxnQDEMhGIVgY-2je-KxRdIJvBT_BehS2XmPlRp_Ii1VgmjPInPm7ayRbLCU5mOs5cBTpcrc61b1t-jCN8WuV-oTBAfGis=s0-d-e1-ft#http://image.xiq.io/returnimage/?url=http://s.thestreet.com/files/tsc/v2008/photos/contrib/uploads/c04279ba-decb-11e9-805f-8d843969e405.png&amp;width=292&amp;height=192&amp;articleid=312578404" alt="Article Heading" class="CToWUd"></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
		<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;border-collapse:collapse">
		<tbody>
		<tr>
		<td style="padding:5.25pt 0in 0in 0in">
		<p class="MsoNormal"></p></td></tr></tbody></table></td></tr></tbody></table></div>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
server.ehlo()
server.starttls()
server.ehlo()
server.login(me,pwd)
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
server.sendmail(me, you, msg.as_string())
server.quit()
