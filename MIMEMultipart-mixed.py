import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# me == my email address
# you == recipient's email address
me = "syedabuzar12@gmail.com" # paste your sender email here
you = "syedabuzar12@gmail.com" # paste recipient email here
pwd = '*******'
# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
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
			<p class="MsoNormal"><a href="https://kbbm6lps.r.us-west-2.awstrack.me/L0/https:%2F%2Fwww.xiqinc.com%2F/1/0101016d68ab2c22-9fe2b45f-3943-452f-922c-118869233441-000000/mrQDW4TDCxkh-dChXN9uFjM7ng0=129" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=https://kbbm6lps.r.us-west-2.awstrack.me/L0/https:%252F%252Fwww.xiqinc.com%252F/1/0101016d68ab2c22-9fe2b45f-3943-452f-922c-118869233441-000000/mrQDW4TDCxkh-dChXN9uFjM7ng0%3D129&amp;source=gmail&amp;ust=1569582956990000&amp;usg=AFQjCNGP9Hy--FPBhVdINsDqPrJ8_qtI-A"><span style="font-family:&quot;Arial&quot;,sans-serif;text-decoration:none"><img border="0" width="102" height="27" style="width:1.0583in;height:.2833in" id="m_-4625585253305646185_x0000_i1069" src="https://ci6.googleusercontent.com/proxy/qP2HaWVr5gSYqCHe5FrxH5vRqIF21KbNUBFmUbu1sr5sSuiemh4QXj2mr0Li8YIzgqMR0QVFygfImtag46da0Go1wNJh3FW_FmijDTZTD9Rw2qfLwXXuvPq7BibDVNg_jvzpc0biaQ=s0-d-e1-ft#https://media.xiq.io/user_images/1562841948_0b800b02-a3c9-11e9-ab34-06b5fc41d42e.png" alt="xiq"></span></a><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
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
			<p class="MsoNormal" align="center" style="text-align:center"><span class="m_-4625585253305646185company"><span style="font-size:8.5pt;color:white;background:black">Alibaba Group Holding Limited
			</span></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			<td width="50%" style="width:50.0%;background:#68b828;padding:3.0pt 3.0pt 3.0pt 3.0pt">
			<p class="MsoNormal" align="center" style="text-align:center"><span class="m_-4625585253305646185category"><span style="font-size:8.5pt;color:white;background:#68b828">Earnings
			</span></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			</tbody>
			</table>
			</div>
			<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif"><img border="0" width="600" height="310" style="width:6.25in;height:3.225in" id="m_-4625585253305646185_x0000_i1068" src="https://ci6.googleusercontent.com/proxy/qSkJzfb6V4i_Zz7otq-t3zLJCKToPAez5v_Vrs4k08LxRgxKhJL4dHhxM9Y-wxVAVcVCtWNSH9QOH-BRAfEZx5l9wS-TjInD7axUrQc5HC4O2u84Mo7urBP98QgKTBw68iyLAdELO70VKLFwxlC4qY9uPIEGy8GhDQWXXukjID6qiD9AM2fCXZqKcjYZsnnRDvPHsphxbI-icw=s0-d-e1-ft#http://image.xiq.io/returnimage/?url=https://images.barrons.com/im-110321?width=1260&amp;size=1.5&amp;width=600&amp;height=310&amp;articleid=312615594" alt="Article Heading"></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
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
			<p class="m_-4625585253305646185description" style="margin-bottom:11.25pt;line-height:12.75pt"><span style="font-size:10.5pt;color:#797e81">Alibaba management maintained its revenue guidance of 500 billion yuan for fiscal 2020. The companys near-term goal is to increase annual active
			consumers from the current 730 million to over one billion in the next five years and nearly double its annual gross merchandise volume from 5.7 trillion yuan in fiscal 2019 to over 10 trillion yuan by 2024. Over the long term, Alibaba (ticker: BABA) wants
			to reach ...</span><a href="http://xiqinc.app.link/?entity=article&amp;source=diq-b25bd71207c44c55bda29d063ac86bb5&amp;id=312615594&amp;url=https://www.barrons.com/articles/alibaba-aims-to-serve-1-billion-customers-a-year-by-2024-51569349858" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Darticle%26source%3Ddiq-b25bd71207c44c55bda29d063ac86bb5%26id%3D312615594%26url%3Dhttps://www.barrons.com/articles/alibaba-aims-to-serve-1-billion-customers-a-year-by-2024-51569349858&amp;source=gmail&amp;ust=1569582956990000&amp;usg=AFQjCNGUtuYPrh0PxafH5ZoCti8XJU8fkA"><b><span style="font-size:10.5pt;color:#9013fe">READ
			MORE</span></b></a><span style="font-size:10.5pt;color:#797e81"> <u></u><u></u></span></p>
			<p class="m_-4625585253305646185time-company" style="line-height:11.25pt"><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">SEP 24, 2019
			</span><span class="m_-4625585253305646185tag-space"><span style="font-size:9.0pt;color:white;letter-spacing:-.25pt;background:white">. . .</span></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt"> |
			</span><span class="m_-4625585253305646185tag-space"><span style="font-size:9.0pt;color:white;letter-spacing:-.25pt;background:white">. . .</span></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">
			</span><span style="font-size:9.0pt;color:#45b5eb;letter-spacing:-.25pt"><a href="http://barrons.com" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://barrons.com&amp;source=gmail&amp;ust=1569582956990000&amp;usg=AFQjCNE8cH34QYafNvJMsANTuo4-seasKQ">barrons.com</a></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">
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
			<p class="MsoNormal"><b><span style="font-family:&quot;Arial&quot;,sans-serif"><img border="0" width="31" height="16" style="width:.325in;height:.1666in" id="m_-4625585253305646185_x0000_i1067" src="https://ci5.googleusercontent.com/proxy/eccw9D_m1___R3eTpcY09b5DonUTXzCbjkqbLpoWY4uVtnUn052yObvaihTw9Rpl49X1pgz6llYFC7oM-irsCE-pOCD61UnVLam6hEaQqD7vmzBUeERDV_faiG8OzArSmsrCB9bJ5g=s0-d-e1-ft#https://media.xiq.io/user_images/1561548164_b7c7ffd0-9804-11e9-8f23-06b5fc41d42e.png" alt="https://media.xiq.io/user_images/1561548164_b7c7ffd0-9804-11e9-8f23-06b5fc41d42e.png"></span></b><b><span style="font-size:15.0pt;font-family:&quot;Arial&quot;,sans-serif;color:white">.</span></b><span class="m_-4625585253305646185pulse-title"><b><span style="font-size:15.0pt;color:black">PULSE</span></b></span><b><span style="font-family:&quot;Arial&quot;,sans-serif">
			<u></u><u></u></span></b></p>
			</td>
			</tr>
			</tbody>
			</table>
			<div>
			<div id="m_-4625585253305646185myTabContent">
			<div id="m_-4625585253305646185home">
			<div>
			<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif;display:none"><u></u>&nbsp;<u></u></span></p>
			<table border="0" cellspacing="0" cellpadding="0" align="left" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
			<tbody>
			<tr style="height:6.75pt">
			<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:6.75pt">
			<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="9" style="width:1.0416in;height:.0916in" id="m_-4625585253305646185_x0000_i1066" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr>
			<td style="padding:0in 0in 0in 0in">
			<p class="MsoNormal"><span class="m_-4625585253305646185text"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">Apple, Inc.</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
			<span class="m_-4625585253305646185count">(15)</span> <span class="m_-4625585253305646185angle-right">&nbsp;</span></span></b><span class="m_-4625585253305646185angle-right"><b><span style="font-size:7.5pt;font-family:&quot;Cambria Math&quot;,serif;color:#001760;text-transform:uppercase">〉</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
			</span></b><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr style="height:2.25pt">
			<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:2.25pt">
			<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="3" style="width:1.0416in;height:.0333in" id="m_-4625585253305646185_x0000_i1065" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
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
			<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="9" style="width:1.0416in;height:.0916in" id="m_-4625585253305646185_x0000_i1064" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr>
			<td style="padding:0in 0in 0in 0in">
			<p class="MsoNormal"><span class="m_-4625585253305646185text"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">Google Inc.</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
			<span class="m_-4625585253305646185count">(12)</span> <span class="m_-4625585253305646185angle-right">&nbsp;</span></span></b><span class="m_-4625585253305646185angle-right"><b><span style="font-size:7.5pt;font-family:&quot;Cambria Math&quot;,serif;color:#001760;text-transform:uppercase">〉</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
			</span></b><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr style="height:2.25pt">
			<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:2.25pt">
			<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="3" style="width:1.0416in;height:.0333in" id="m_-4625585253305646185_x0000_i1063" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
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
			<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="9" style="width:1.0416in;height:.0916in" id="m_-4625585253305646185_x0000_i1062" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr>
			<td style="padding:0in 0in 0in 0in">
			<p class="MsoNormal"><span class="m_-4625585253305646185text"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">Accenture plc
			</span></b></span><span class="m_-4625585253305646185count"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">(8)</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
			<span class="m_-4625585253305646185angle-right">&nbsp;</span></span></b><span class="m_-4625585253305646185angle-right"><b><span style="font-size:7.5pt;font-family:&quot;Cambria Math&quot;,serif;color:#001760;text-transform:uppercase">〉</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
			</span></b><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr style="height:2.25pt">
			<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:2.25pt">
			<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="3" style="width:1.0416in;height:.0333in" id="m_-4625585253305646185_x0000_i1061" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
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
			<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="9" style="width:1.0416in;height:.0916in" id="m_-4625585253305646185_x0000_i1060" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr>
			<td style="padding:0in 0in 0in 0in">
			<p class="MsoNormal"><span class="m_-4625585253305646185text"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">Alibaba Group Holding Limited
			</span></b></span><span class="m_-4625585253305646185count"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">(8)</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
			<span class="m_-4625585253305646185angle-right">&nbsp;</span></span></b><span class="m_-4625585253305646185angle-right"><b><span style="font-size:7.5pt;font-family:&quot;Cambria Math&quot;,serif;color:#001760;text-transform:uppercase">〉</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
			</span></b><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr style="height:2.25pt">
			<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:2.25pt">
			<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="3" style="width:1.0416in;height:.0333in" id="m_-4625585253305646185_x0000_i1059" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
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
			<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="9" style="width:1.0416in;height:.0916in" id="m_-4625585253305646185_x0000_i1058" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr>
			<td style="padding:0in 0in 0in 0in">
			<p class="MsoNormal"><span class="m_-4625585253305646185text"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">Twitter, Inc.</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
			<span class="m_-4625585253305646185count">(5)</span> <span class="m_-4625585253305646185angle-right">&nbsp;</span></span></b><span class="m_-4625585253305646185angle-right"><b><span style="font-size:7.5pt;font-family:&quot;Cambria Math&quot;,serif;color:#001760;text-transform:uppercase">〉</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
			</span></b><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr style="height:2.25pt">
			<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:2.25pt">
			<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="3" style="width:1.0416in;height:.0333in" id="m_-4625585253305646185_x0000_i1057" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
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
			<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="9" style="width:1.0416in;height:.0916in" id="m_-4625585253305646185_x0000_i1056" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr>
			<td style="padding:0in 0in 0in 0in">
			<p class="MsoNormal"><span class="m_-4625585253305646185text"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">Dell, Inc.</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
			<span class="m_-4625585253305646185count">(4)</span> <span class="m_-4625585253305646185angle-right">&nbsp;</span></span></b><span class="m_-4625585253305646185angle-right"><b><span style="font-size:7.5pt;font-family:&quot;Cambria Math&quot;,serif;color:#001760;text-transform:uppercase">〉</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
			</span></b><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr style="height:2.25pt">
			<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:2.25pt">
			<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="3" style="width:1.0416in;height:.0333in" id="m_-4625585253305646185_x0000_i1055" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
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
			<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="9" style="width:1.0416in;height:.0916in" id="m_-4625585253305646185_x0000_i1054" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr>
			<td style="padding:0in 0in 0in 0in">
			<p class="MsoNormal"><span class="m_-4625585253305646185text"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">Microsoft Corporation</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
			<span class="m_-4625585253305646185count">(4)</span> <span class="m_-4625585253305646185angle-right">&nbsp;</span></span></b><span class="m_-4625585253305646185angle-right"><b><span style="font-size:7.5pt;font-family:&quot;Cambria Math&quot;,serif;color:#001760;text-transform:uppercase">〉</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
			</span></b><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr style="height:2.25pt">
			<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:2.25pt">
			<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="3" style="width:1.0416in;height:.0333in" id="m_-4625585253305646185_x0000_i1053" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
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
			<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="9" style="width:1.0416in;height:.0916in" id="m_-4625585253305646185_x0000_i1052" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr>
			<td style="padding:0in 0in 0in 0in">
			<p class="MsoNormal"><span class="m_-4625585253305646185text"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">Facebook, Inc.</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
			<span class="m_-4625585253305646185count">(2)</span> <span class="m_-4625585253305646185angle-right">&nbsp;</span></span></b><span class="m_-4625585253305646185angle-right"><b><span style="font-size:7.5pt;font-family:&quot;Cambria Math&quot;,serif;color:#001760;text-transform:uppercase">〉</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
			</span></b><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr style="height:2.25pt">
			<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:2.25pt">
			<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="3" style="width:1.0416in;height:.0333in" id="m_-4625585253305646185_x0000_i1051" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
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
			<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="9" style="width:1.0416in;height:.0916in" id="m_-4625585253305646185_x0000_i1050" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr>
			<td style="padding:0in 0in 0in 0in">
			<p class="MsoNormal"><span class="m_-4625585253305646185text"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">Genpact Ltd.
			</span></b></span><span class="m_-4625585253305646185count"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">(2)</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
			<span class="m_-4625585253305646185angle-right">&nbsp;</span></span></b><span class="m_-4625585253305646185angle-right"><b><span style="font-size:7.5pt;font-family:&quot;Cambria Math&quot;,serif;color:#001760;text-transform:uppercase">〉</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
			</span></b><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr style="height:2.25pt">
			<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:2.25pt">
			<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="3" style="width:1.0416in;height:.0333in" id="m_-4625585253305646185_x0000_i1049" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
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
			<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="9" style="width:1.0416in;height:.0916in" id="m_-4625585253305646185_x0000_i1048" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr>
			<td style="padding:0in 0in 0in 0in">
			<p class="MsoNormal"><span class="m_-4625585253305646185text"><b><span style="font-size:7.5pt;color:#001760;text-transform:uppercase">Oracle Corp</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
			<span class="m_-4625585253305646185count">(2)</span> <span class="m_-4625585253305646185angle-right">&nbsp;</span></span></b><span class="m_-4625585253305646185angle-right"><b><span style="font-size:7.5pt;font-family:&quot;Cambria Math&quot;,serif;color:#001760;text-transform:uppercase">〉</span></b></span><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#001760;text-transform:uppercase">
			</span></b><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr style="height:2.25pt">
			<td width="100%" style="width:100.0%;padding:0in 0in 0in 0in;height:2.25pt">
			<p class="MsoNormal"><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><img border="0" width="100" height="3" style="width:1.0416in;height:.0333in" id="m_-4625585253305646185_x0000_i1047" src="https://ci6.googleusercontent.com/proxy/377y6-Jl7g2KABwAx-cxSGThHs1ORDfWsLPBcXofnxzzyIw4jEq77uYUu-BIKU3nEvOdszGGEN_X7v92y744CqbfCXq9FifnZOB012Lf-vO_3T1gyIrQ5c3x71JChfcNrusslQvvBw=s0-d-e1-ft#https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg" alt="https://media.xiq.io/user_images/1561617917_1ffa2284-98a7-11e9-bcdd-06b5fc41d42e.jpg"></span><span style="font-size:1.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white"><u></u><u></u></span></p>
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
			<p class="MsoNormal" align="center" style="text-align:center"><span class="m_-4625585253305646185company"><span style="font-size:8.5pt;color:white;background:black">Accenture plc
			</span></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			<td width="50%" style="width:50.0%;background:#d64025;padding:3.0pt 3.0pt 3.0pt 3.0pt">
			<p class="MsoNormal" align="center" style="text-align:center"><span class="m_-4625585253305646185category"><span style="font-size:8.5pt;color:white;background:#d64025">CxO Moves
			</span></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			</tbody>
			</table>
			</div>
			<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif"><img border="0" width="292" height="192" style="width:3.0416in;height:2.0in" id="m_-4625585253305646185_x0000_i1046" src="https://ci4.googleusercontent.com/proxy/aVvPDxKLKaV1_4fb0YyQe98ryFQ8twXR6lAiMLD6wQcRNdu1PxuRSQuSie9s8_Ww6x-pHGia9OZLBTlE7AimC0JKRc58-YFviA8cF93uWaj-QiSlAcbMHvCOqYc2QggkAd4ORXlVajRJSoE_wT28cSt4_gTXyhCwN7snWuZpNAuTChotiMWpV2rSM1c3zbtNpJ8nSCjrVxVn-Hre2NP64WTAaYuyJXwghh6aDTyoOtZU4Apu2DT5TZgzIePxbN9KKjRJI42HP7eC6kUySqfsQiPly4ekoI-B=s0-d-e1-ft#http://image.xiq.io/returnimage/?url=http://ec2-54-200-50-167.us-west-2.compute.amazonaws.com/static/admin/upload/542b85b2-df14-11e9-a117-06945eaf9ebf.jpeg&amp;width=292&amp;height=192&amp;articleid=312579976" alt="Article Heading"></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
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
			<p class="m_-4625585253305646185description" style="margin-bottom:11.25pt;line-height:12.75pt"><span style="font-size:10.5pt;color:#797e81">NEW YORK; Sept. 24, 2019 Accenture (NYSE: ACN) has appointed Simon Eaves as group chief executive ...
			</span><a href="http://xiqinc.app.link/?entity=article&amp;source=diq-b25bd71207c44c55bda29d063ac86bb5&amp;id=312579976&amp;url=https://newsroom.accenture.com/news/accenture-names-simon-eaves-group-chief-executive-products-succeeding-sander-van-t-noordende.htm" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Darticle%26source%3Ddiq-b25bd71207c44c55bda29d063ac86bb5%26id%3D312579976%26url%3Dhttps://newsroom.accenture.com/news/accenture-names-simon-eaves-group-chief-executive-products-succeeding-sander-van-t-noordende.htm&amp;source=gmail&amp;ust=1569582956992000&amp;usg=AFQjCNFhJ3zSqFQB4XKx-sqVgC2YmO8e8w"><b><span style="font-size:10.5pt;color:#9013fe">READ
			MORE</span></b></a><span style="font-size:10.5pt;color:#797e81"> <u></u><u></u></span></p>
			<p class="m_-4625585253305646185time-company" style="line-height:11.25pt"><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">SEP 24, 2019
			</span><span class="m_-4625585253305646185tag-space"><span style="font-size:9.0pt;color:white;letter-spacing:-.25pt;background:white">. . .</span></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt"> |
			</span><span class="m_-4625585253305646185tag-space"><span style="font-size:9.0pt;color:white;letter-spacing:-.25pt;background:white">. . .</span></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">
			</span><span style="font-size:9.0pt;color:#45b5eb;letter-spacing:-.25pt"><a href="http://newsroom.accenture.com" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://newsroom.accenture.com&amp;source=gmail&amp;ust=1569582956992000&amp;usg=AFQjCNHpKCvJocI0lwWVLmtvn2m_jhWk4Q">newsroom.accenture.com</a></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">
			<u></u><u></u></span></p>
			</td>
			</tr>
			</tbody>
			</table>
			</td>
			</tr>
			<tr>
			<td colspan="2" style="padding:0in 0in 0in 0in">
			<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif"><img border="0" width="600" height="62" style="width:6.25in;height:.6416in" id="m_-4625585253305646185_x0000_i1045" src="https://ci4.googleusercontent.com/proxy/ZvYaY0nzldgo9E9Q5P3M7O3PSyZ5I2BS83qxTsvS9QmG6y73YhQ0TLWGEy8hUWmbPOLrWqaTIJHyFjboZ2KLY3XpyoZHj5q7T9yDgwuK2TXZxwD4CfUHTDr1ZOIH6581wYxWKWxhSg=s0-d-e1-ft#https://media.xiq.io/user_images/1563360050_58120730-a87f-11e9-94d5-06b5fc41d42e.png" alt="https://media.xiq.io/user_images/1563360050_58120730-a87f-11e9-94d5-06b5fc41d42e.png"></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr>
			<td colspan="2" valign="top" style="padding:0in 0in 18.75pt 0in">
			<div align="center">
			<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
			<tbody>
			<tr>
			<td width="50%" style="width:50.0%;background:black;padding:3.0pt 3.0pt 3.0pt 3.0pt">
			<p class="MsoNormal" align="center" style="text-align:center"><span class="m_-4625585253305646185company"><span style="font-size:8.5pt;color:white;background:black">Facebook, Inc.
			</span></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			<td width="50%" style="width:50.0%;background:#8dc63f;padding:3.0pt 3.0pt 3.0pt 3.0pt">
			<p class="MsoNormal" align="center" style="text-align:center"><span class="m_-4625585253305646185category"><span style="font-size:8.5pt;color:white;background:#8dc63f">M&amp;A
			</span></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			</tbody>
			</table>
			</div>
			<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif"><img border="0" width="600" height="310" style="width:6.25in;height:3.225in" id="m_-4625585253305646185_x0000_i1044" src="https://ci5.googleusercontent.com/proxy/w9L7lTTneWyk5zd3V6ma2YP58uvv3SS-lil0wXtVAy1Q5wh9XH34sspztxKEqOqBhSPtBYJsDkT43MDIZsb1xcNvh2eqf56Gg07nJMda15uyBHCkgcqiFodyMuobECapHeHm0TLsko6i6b-EdmVW50PLJiMvYF0TG8gp3IKzmxIzHydbz3H0W7bfNyhcuDuN23ldJRr3OtVQvQQqYd4SCH3JosJkcCkVnJsut7fJZHPztzSCyYfSKE5zupKHxT0JjDIS=s0-d-e1-ft#http://image.xiq.io/returnimage/?url=https://content.fortune.com/wp-content/uploads/2019/09/GettyImages-1170810085.jpg?resize=1200,600&amp;width=600&amp;height=310&amp;articleid=312621537" alt="Article Heading"></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
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
			<p class="m_-4625585253305646185description" style="margin-bottom:11.25pt;line-height:12.75pt"><span style="font-size:10.5pt;color:#797e81">Facebook Inc. sent a clear signal with its agreement to buy a brain computing startup: heightened regulatory scrutiny and intensifying antitrust
			probes wont slow down its pace of acquisitions. With its announcement Monday of plans to purchase CTRL-Labs for at least $500 million, Facebook continued its pattern ...</span><a href="http://xiqinc.app.link/?entity=article&amp;source=diq-b25bd71207c44c55bda29d063ac86bb5&amp;id=312621537&amp;url=https://fortune.com/2019/09/25/facebook-ctrl-labs-ftc-antitrust/" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Darticle%26source%3Ddiq-b25bd71207c44c55bda29d063ac86bb5%26id%3D312621537%26url%3Dhttps://fortune.com/2019/09/25/facebook-ctrl-labs-ftc-antitrust/&amp;source=gmail&amp;ust=1569582956992000&amp;usg=AFQjCNG8hGnCj-I_O6ZwUcOGpTGcTALFkw"><b><span style="font-size:10.5pt;color:#9013fe">READ
			MORE</span></b></a><span style="font-size:10.5pt;color:#797e81"> <u></u><u></u></span></p>
			<p class="m_-4625585253305646185time-company" style="line-height:11.25pt"><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">SEP 25, 2019
			</span><span class="m_-4625585253305646185tag-space"><span style="font-size:9.0pt;color:white;letter-spacing:-.25pt;background:white">. . .</span></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt"> |
			</span><span class="m_-4625585253305646185tag-space"><span style="font-size:9.0pt;color:white;letter-spacing:-.25pt;background:white">. . .</span></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">
			</span><span style="font-size:9.0pt;color:#45b5eb;letter-spacing:-.25pt"><a href="http://fortune.com" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://fortune.com&amp;source=gmail&amp;ust=1569582956992000&amp;usg=AFQjCNHYoIoLJ8TYXyBDN56HVBrMSxC8ow">fortune.com</a></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">
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
			<p class="MsoNormal" align="center" style="text-align:center"><span class="m_-4625585253305646185company"><span style="font-size:8.5pt;color:white;background:black">Oracle Corp
			</span></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			<td width="50%" style="width:50.0%;background:#ff484b;padding:3.0pt 3.0pt 3.0pt 3.0pt">
			<p class="MsoNormal" align="center" style="text-align:center"><span class="m_-4625585253305646185category"><span style="font-size:8.5pt;color:white;background:#ff484b">CxO News
			</span></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			</tbody>
			</table>
			</div>
			<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif"><img border="0" width="292" height="192" style="width:3.0416in;height:2.0in" id="m_-4625585253305646185_x0000_i1043" src="https://ci3.googleusercontent.com/proxy/6uA4oilYtmgPDzC5bwvtf28bGwyz7-ES90li0H64gX5S6w4ePslNQNTk87HzO0KrVE6CEkmtI3RT0cQNwU1yGzxADkO8zXTmxA3fbg70T481J9d1M1hXotuZ5khD_E79ohz29--iDAjwiTnaK38RSF6E-oPWyoFBMuiBbuk644-9CoxnQDEMhGIVgY-2je-KxRdIJvBT_BehS2XmPlRp_Ii1VgmjPInPm7ayRbLCU5mOs5cBTpcrc61b1t-jCN8WuV-oTBAfGis=s0-d-e1-ft#http://image.xiq.io/returnimage/?url=http://s.thestreet.com/files/tsc/v2008/photos/contrib/uploads/c04279ba-decb-11e9-805f-8d843969e405.png&amp;width=292&amp;height=192&amp;articleid=312578404" alt="Article Heading"></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;border-collapse:collapse">
			<tbody>
			<tr>
			<td style="padding:5.25pt 0in 0in 0in">
			<p class="MsoNormal"><b><span style="font-size:15.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#30374e">What Is Larry Ellison's Net Worth?</span></b><b><span style="font-size:15.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#222222">
			<u></u><u></u></span></b></p>
			</td>
			</tr>
			<tr>
			<td valign="top" style="padding:3.75pt 0in 3.75pt 0in">
			<p class="m_-4625585253305646185description" style="margin-bottom:11.25pt;line-height:12.75pt"><span style="font-size:10.5pt;color:#797e81">Larry Ellison, the founder of the technology giant Oracle (ORCL - Get Report) , is reportedly worth $65.7 billion - that's billion with a "b."
			That figure ... </span><a href="http://xiqinc.app.link/?entity=article&amp;source=diq-b25bd71207c44c55bda29d063ac86bb5&amp;id=312578404&amp;url=https://www.thestreet.com/lifestyle/larry-ellison-net-worth-15100634" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Darticle%26source%3Ddiq-b25bd71207c44c55bda29d063ac86bb5%26id%3D312578404%26url%3Dhttps://www.thestreet.com/lifestyle/larry-ellison-net-worth-15100634&amp;source=gmail&amp;ust=1569582956992000&amp;usg=AFQjCNEySB1xwnmAP3cBbg1GZH5YjVlHVw"><b><span style="font-size:10.5pt;color:#9013fe">READ
			MORE</span></b></a><span style="font-size:10.5pt;color:#797e81"> <u></u><u></u></span></p>
			<p class="m_-4625585253305646185time-company" style="line-height:11.25pt"><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">SEP 24, 2019
			</span><span class="m_-4625585253305646185tag-space"><span style="font-size:9.0pt;color:white;letter-spacing:-.25pt;background:white">. . .</span></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt"> |
			</span><span class="m_-4625585253305646185tag-space"><span style="font-size:9.0pt;color:white;letter-spacing:-.25pt;background:white">. . .</span></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">
			</span><span style="font-size:9.0pt;color:#45b5eb;letter-spacing:-.25pt"><a href="http://thestreet.com" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://thestreet.com&amp;source=gmail&amp;ust=1569582956993000&amp;usg=AFQjCNH7PbHfa6G-f-fY1fO_iOYZ7f5DJw">thestreet.com</a></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">
			<u></u><u></u></span></p>
			</td>
			</tr>
			</tbody>
			</table>
			</td>
			<td width="50%" valign="top" style="width:50.0%;padding:0in 0in 18.75pt 6.0pt">
			<div align="center">
			<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
			<tbody>
			<tr>
			<td width="50%" style="width:50.0%;background:black;padding:3.0pt 3.0pt 3.0pt 3.0pt">
			<p class="MsoNormal" align="center" style="text-align:center"><span class="m_-4625585253305646185company"><span style="font-size:8.5pt;color:white;background:black">Google Inc.
			</span></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			<td width="50%" style="width:50.0%;background:#00b19d;padding:3.0pt 3.0pt 3.0pt 3.0pt">
			<p class="MsoNormal" align="center" style="text-align:center"><span class="m_-4625585253305646185category"><span style="font-size:8.5pt;color:white;background:#00b19d">Legal
			</span></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			</tbody>
			</table>
			</div>
			<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif"><img border="0" width="292" height="192" style="width:3.0416in;height:2.0in" id="m_-4625585253305646185_x0000_i1042" src="https://ci5.googleusercontent.com/proxy/zZFmSQGqbL4D9gNna6pD3rk6NU0lJJYiVUnF4XN9nkeMQj3kP01Njowws6n_4div72C_r3F_abO9LXjVr2-QUYUEO0eKLlEJ_6bNZKGbzcfZGXHkRuIgNKdwdW3LMQSRu4MCuHAHJbW5poOUd3qWPoCO-hf7hBtsfmIMgBsvCJKhaz_OGmLMgj8cw5j2Cg-WEd6k9EJY3fV5iXlxuGJrWA=s0-d-e1-ft#http://image.xiq.io/returnimage/?url=https://regmedia.co.uk/2019/09/25/shutterstock_thumbs_down.jpg&amp;width=292&amp;height=192&amp;articleid=312609773" alt="Article Heading"></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;border-collapse:collapse">
			<tbody>
			<tr>
			<td style="padding:5.25pt 0in 0in 0in">
			<p class="MsoNormal"><b><span style="font-size:15.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#30374e">Google Takes Sole Stand on Privacy, Rejects New Rules for Fear of ...</span></b><b><span style="font-size:15.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#222222">
			<u></u><u></u></span></b></p>
			</td>
			</tr>
			<tr>
			<td valign="top" style="padding:3.75pt 0in 3.75pt 0in">
			<p class="m_-4625585253305646185description" style="margin-bottom:11.25pt;line-height:12.75pt"><span style="font-size:10.5pt;color:#797e81">Google has blocked a proposed revision of the charter of the Privacy Interest Group (PING), a part of the W3C web ...
			</span><a href="http://xiqinc.app.link/?entity=article&amp;source=diq-b25bd71207c44c55bda29d063ac86bb5&amp;id=312609773&amp;url=https://www.theregister.co.uk/2019/09/25/google_privacy_wc3/" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Darticle%26source%3Ddiq-b25bd71207c44c55bda29d063ac86bb5%26id%3D312609773%26url%3Dhttps://www.theregister.co.uk/2019/09/25/google_privacy_wc3/&amp;source=gmail&amp;ust=1569582956993000&amp;usg=AFQjCNErWoG3NGyFZevVescVAKGtIfrxyQ"><b><span style="font-size:10.5pt;color:#9013fe">READ MORE</span></b></a><span style="font-size:10.5pt;color:#797e81">
			<u></u><u></u></span></p>
			<p class="m_-4625585253305646185time-company" style="line-height:11.25pt"><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">SEP 25, 2019
			</span><span class="m_-4625585253305646185tag-space"><span style="font-size:9.0pt;color:white;letter-spacing:-.25pt;background:white">. . .</span></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt"> |
			</span><span class="m_-4625585253305646185tag-space"><span style="font-size:9.0pt;color:white;letter-spacing:-.25pt;background:white">. . .</span></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">
			</span><span style="font-size:9.0pt;color:#45b5eb;letter-spacing:-.25pt"><a href="http://theregister.co.uk" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://theregister.co.uk&amp;source=gmail&amp;ust=1569582956993000&amp;usg=AFQjCNHQoJbR17uxtP6Cb4sTPGopkZmukw">theregister.co.uk</a></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">
			<u></u><u></u></span></p>
			</td>
			</tr>
			</tbody>
			</table>
			</td>
			</tr>
			<tr>
			<td colspan="2" valign="top" style="padding:0in 0in 18.75pt 0in">
			<div align="center">
			<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;background:white;border-collapse:collapse">
			<tbody>
			<tr>
			<td width="50%" style="width:50.0%;background:black;padding:3.0pt 3.0pt 3.0pt 3.0pt">
			<p class="MsoNormal" align="center" style="text-align:center"><span class="m_-4625585253305646185company"><span style="font-size:8.5pt;color:white;background:black">Dell, Inc.
			</span></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			<td width="50%" style="width:50.0%;background:#4483ea;padding:3.0pt 3.0pt 3.0pt 3.0pt">
			<p class="MsoNormal" align="center" style="text-align:center"><span class="m_-4625585253305646185category"><span style="font-size:8.5pt;color:white;background:#4483ea">Strategy
			</span></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			</tbody>
			</table>
			</div>
			<p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif"><img border="0" width="600" height="310" style="width:6.25in;height:3.225in" id="m_-4625585253305646185_x0000_i1041" src="https://ci4.googleusercontent.com/proxy/7JJwvKBYPPx18xxoadYiByDWw3ZG3tRQ8kOEIbz-6jIah5l7pvlepT7YnHTvQgOzrxb57QHqsxOPbsLUqFa62YgsolQGZn2dbXARp70SCim05aPMcpZYwtBasQT0dJzMQOYG_JhNmnOdKTuiWBR_VGVXonlsCGBKgfBb6yLzpbBIhah0noI0AzyDQIQLB5VqNDYfaE3x5QEMOTSThz7ualdG9UtHGQ=s0-d-e1-ft#http://image.xiq.io/returnimage/?url=https://cdn.mos.cms.futurecdn.net/8j3gApKZP5NRsXM8jpKT9V-1024-80.jpg&amp;width=600&amp;height=310&amp;articleid=312496958" alt="Article Heading"></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;border-collapse:collapse">
			<tbody>
			<tr>
			<td style="padding:5.25pt 0in 0in 0in">
			<p class="MsoNormal"><b><span style="font-size:15.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#30374e">How Dell Is Empowering SMBs in India With a Wave of Innovative Products and Services</span></b><b><span style="font-size:15.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#222222">
			<u></u><u></u></span></b></p>
			</td>
			</tr>
			<tr>
			<td valign="top" style="padding:3.75pt 0in 3.75pt 0in">
			<p class="m_-4625585253305646185description" style="margin-bottom:11.25pt;line-height:12.75pt"><span style="font-size:10.5pt;color:#797e81">A business is as good as the products and services it offers. In India, small and medium businesses (SMBs) are eyeing digitisation which prove
			to be a $80-billion opportunity by 2024. This is according to Zinnov, a managment consultancy. In fact, more than 75 million SMBs are expected to spend between $14-$16 billion on ...</span><a href="http://xiqinc.app.link/?entity=article&amp;source=diq-b25bd71207c44c55bda29d063ac86bb5&amp;id=312496958&amp;url=https://www.techradar.com/news/how-dell-is-empowering-smbs-in-india-with-a-wave-of-innovative-products-and-services" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Darticle%26source%3Ddiq-b25bd71207c44c55bda29d063ac86bb5%26id%3D312496958%26url%3Dhttps://www.techradar.com/news/how-dell-is-empowering-smbs-in-india-with-a-wave-of-innovative-products-and-services&amp;source=gmail&amp;ust=1569582956993000&amp;usg=AFQjCNECwVUbWqKCg9JoaybJlUGIFtXQiw"><b><span style="font-size:10.5pt;color:#9013fe">READ
			MORE</span></b></a><span style="font-size:10.5pt;color:#797e81"> <u></u><u></u></span></p>
			<p class="m_-4625585253305646185time-company" style="line-height:11.25pt"><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">SEP 24, 2019
			</span><span class="m_-4625585253305646185tag-space"><span style="font-size:9.0pt;color:white;letter-spacing:-.25pt;background:white">. . .</span></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt"> |
			</span><span class="m_-4625585253305646185tag-space"><span style="font-size:9.0pt;color:white;letter-spacing:-.25pt;background:white">. . .</span></span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt">
			</span><span style="font-size:9.0pt;color:#45b5eb;letter-spacing:-.25pt"><a href="http://techradar.com" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://techradar.com&amp;source=gmail&amp;ust=1569582956993000&amp;usg=AFQjCNGHwCsyWhphY7A0ZeqAFRgY-UGFDw">techradar.com</a>
			</span><span style="font-size:9.0pt;color:#93a4ba;letter-spacing:-.25pt"><u></u><u></u></span></p>
			</td>
			</tr>
			</tbody>
			</table>
			</td>
			</tr>
			<tr>
			<td colspan="2" style="padding:21.0pt 0in 33.75pt 0in">
			<p class="MsoNormal" align="center" style="text-align:center"><a href="http://xiqinc.app.link/?entity=widget&amp;source=diq&amp;type=alert_feeds&amp;category=Sales%20Triggers&amp;title=Sales%20Triggers" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Dwidget%26source%3Ddiq%26type%3Dalert_feeds%26category%3DSales%2520Triggers%26title%3DSales%2520Triggers&amp;source=gmail&amp;ust=1569582956993000&amp;usg=AFQjCNHrgAv6TLiaYrVhVSsVV-B_CxJxhw"><span style="font-size:13.5pt;font-family:&quot;Arial&quot;,sans-serif;color:white;text-transform:uppercase;text-decoration:none"><img border="0" width="300" height="50" style="width:3.125in;height:.525in" id="m_-4625585253305646185_x0000_i1040" src="https://ci4.googleusercontent.com/proxy/JNTk865I63QXPCE_e_yGxGeLMvOhz_S7H1XEB7SPWZ7gU7zApryOGEtgjNP4uBDalziIwdmOX5tWyJ5E9NXeUcx4qHmRLFEegzND2DGxdmDx8xz7pukHRl16RKSao5Hti4YzfUdG4Q=s0-d-e1-ft#https://media.xiq.io/user_images/1563102966_c655baf6-a628-11e9-9ec7-06b5fc41d42e.png" alt="https://media.xiq.io/user_images/1563102966_c655baf6-a628-11e9-9ec7-06b5fc41d42e.png"></span></a><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr>
			<td width="33%" colspan="2" style="width:33.32%;padding:3.75pt 0in 37.5pt 0in">
			<p class="MsoNormal" align="center" style="text-align:center"><a href="https://kbbm6lps.r.us-west-2.awstrack.me/L0/https:%2F%2Fxiqinc.com%2Fschedule-a-demo%2F/1/0101016d68ab2c22-9fe2b45f-3943-452f-922c-118869233441-000000/BnmXsiT1zK8AW93bmzU3dkUUfVw=129" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=https://kbbm6lps.r.us-west-2.awstrack.me/L0/https:%252F%252Fxiqinc.com%252Fschedule-a-demo%252F/1/0101016d68ab2c22-9fe2b45f-3943-452f-922c-118869233441-000000/BnmXsiT1zK8AW93bmzU3dkUUfVw%3D129&amp;source=gmail&amp;ust=1569582956993000&amp;usg=AFQjCNE1de31Enub6TDC5TA3PVu8mowSdg"><span style="font-family:&quot;Arial&quot;,sans-serif;text-decoration:none"><img border="0" width="600" height="150" style="width:6.25in;height:1.5666in" id="m_-4625585253305646185_x0000_i1039" src="https://ci6.googleusercontent.com/proxy/NIUSpfq_omKeHM-xINlpXnvscrITN7mvmPY0joWloat9SHTjUzGCuTa_3Lb8KCsxhEeWP2-tEGwpDKw0aKiOs5kc2iPAm_VjvfmplahIwZy9OeHS5DqBctwd=s0-d-e1-ft#https://s3-us-west-2.amazonaws.com/xiqapp-static/Daily_IQ_Banners/6.png" alt="xiq baner"></span></a><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr>
			<td colspan="2" style="padding:0in 0in 30.0pt 0in">
			<p class="MsoNormal" align="center" style="text-align:center"><a href="http://xiqinc.app.link/?entity=widget&amp;source=diq&amp;type=people&amp;category=Executives&amp;title=CxO%20Tweets" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Dwidget%26source%3Ddiq%26type%3Dpeople%26category%3DExecutives%26title%3DCxO%2520Tweets&amp;source=gmail&amp;ust=1569582956993000&amp;usg=AFQjCNECxW3siEf-opT6j8qPjF9J_MqWXw"><b><span style="font-size:21.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#f5a623;letter-spacing:-.6pt;text-decoration:none">CxO
			Tweets</span></b></a><span style="font-family:&quot;Arial&quot;,sans-serif"> <u></u><u></u></span></p>
			</td>
			</tr>
			<tr>
			<td width="50%" style="width:50.0%;padding:0in 6.0pt 37.5pt 22.5pt">
			<div align="center">
			<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;border-collapse:collapse">
			<tbody>
			<tr>
			<td width="80" style="width:60.0pt;padding:0in 0in 0in 0in">
			<p class="MsoNormal"><a href="http://xiqinc.app.link/?entity=person&amp;source=diq&amp;id=288012&amp;title=Parag%20Agrawal" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Dperson%26source%3Ddiq%26id%3D288012%26title%3DParag%2520Agrawal&amp;source=gmail&amp;ust=1569582956993000&amp;usg=AFQjCNHH1rvMfQ9K-Usglhs5wyVE7M9NLw"><span style="font-family:&quot;Arial&quot;,sans-serif;text-decoration:none"><img border="0" width="60" height="60" style="width:.625in;height:.625in" id="m_-4625585253305646185_x0000_i1038" src="https://ci4.googleusercontent.com/proxy/28L-q0ijdTuoa-Ycwi0hAQldbpXyzL9pvTHIzmvZVyhDyHbk-ePYfrAsr81ySj38DVdmYkG6bLWXbc1OHK9cPBLyDroV_UJ7tWvHBsurGgHSBK03RoPL2gXuXTrOssByJRSYBbH-=s0-d-e1-ft#https://s3-us-west-2.amazonaws.com/xiqapp-static/Persons/parag_agrawal_5a14742a.jpg" alt="cxo"></span></a><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			<td style="padding:0in 0in 0in 0in">
			<p class="m_-4625585253305646185cxo-name" style="line-height:15.75pt"><a href="http://xiqinc.app.link/?entity=person&amp;source=diq&amp;id=288012&amp;title=Parag%20Agrawal" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Dperson%26source%3Ddiq%26id%3D288012%26title%3DParag%2520Agrawal&amp;source=gmail&amp;ust=1569582956994000&amp;usg=AFQjCNEphr5bY-0IG3AdCBMw2ryH7vIv0Q"><b><span style="font-size:13.5pt;color:#333333">Parag Agrawal</span></b></a><b><span style="font-size:13.5pt"><u></u><u></u></span></b></p>
			<p class="MsoNormal"><span class="m_-4625585253305646185cxo-position"><span style="font-size:9.0pt;color:#8d8d8d">CTO</span></span><span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#8d8d8d"><br>
			</span><span class="m_-4625585253305646185cxo-company"><b><span style="font-size:10.5pt">Twitter, Inc.</span></b></span><span style="font-family:&quot;Arial&quot;,sans-serif">
			<u></u><u></u></span></p>
			</td>
			</tr>
			</tbody>
			</table>
			</div>
			</td>
			<td width="50%" style="width:50.0%;padding:0in 22.5pt 37.5pt 6.0pt">
			<div align="center">
			<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;border-collapse:collapse">
			<tbody>
			<tr>
			<td width="80" style="width:60.0pt;padding:0in 0in 0in 0in">
			<p class="MsoNormal"><a href="http://xiqinc.app.link/?entity=person&amp;source=diq&amp;id=314986&amp;title=Michael%20Montano" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Dperson%26source%3Ddiq%26id%3D314986%26title%3DMichael%2520Montano&amp;source=gmail&amp;ust=1569582956994000&amp;usg=AFQjCNFsZQns52uElwogkVjXQU1-iZWazA"><span style="font-family:&quot;Arial&quot;,sans-serif;text-decoration:none"><img border="0" width="60" height="60" style="width:.625in;height:.625in" id="m_-4625585253305646185_x0000_i1037" src="https://ci3.googleusercontent.com/proxy/50KQ8sZXtlBTSzNe_qt_8jZQJzYWzILlG6MQHty_Tn4ZkGtNXl_s-JdyeHaFTh7zvYEH0VbN-HMfeQ9HjZ-y4J5cBFCv4skQrCn1B9wJ33t1dBSL-vrRbJhGDg=s0-d-e1-ft#https://s3-us-west-2.amazonaws.com/xiqapp-static/Persons/mikemontano.jpg" alt="cxo"></span></a><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			<td style="padding:0in 0in 0in 0in">
			<p class="m_-4625585253305646185cxo-name" style="line-height:15.75pt"><a href="http://xiqinc.app.link/?entity=person&amp;source=diq&amp;id=314986&amp;title=Michael%20Montano" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Dperson%26source%3Ddiq%26id%3D314986%26title%3DMichael%2520Montano&amp;source=gmail&amp;ust=1569582956994000&amp;usg=AFQjCNFsZQns52uElwogkVjXQU1-iZWazA"><b><span style="font-size:13.5pt;color:#333333">Michael Montano</span></b></a><b><span style="font-size:13.5pt"><u></u><u></u></span></b></p>
			<p class="MsoNormal"><span class="m_-4625585253305646185cxo-position"><span style="font-size:9.0pt;color:#8d8d8d">Engineering Lead</span></span><span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#8d8d8d"><br>
			</span><span class="m_-4625585253305646185cxo-company"><b><span style="font-size:10.5pt">Twitter, Inc.</span></b></span><span style="font-family:&quot;Arial&quot;,sans-serif">
			<u></u><u></u></span></p>
			</td>
			</tr>
			</tbody>
			</table>
			</div>
			</td>
			</tr>
			<tr>
			<td width="50%" style="width:50.0%;padding:0in 6.0pt 37.5pt 22.5pt">
			<div align="center">
			<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;border-collapse:collapse">
			<tbody>
			<tr>
			<td width="80" style="width:60.0pt;padding:0in 0in 0in 0in">
			<p class="MsoNormal"><a href="http://xiqinc.app.link/?entity=person&amp;source=diq&amp;id=288400&amp;title=NV%20Tyagarajan" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Dperson%26source%3Ddiq%26id%3D288400%26title%3DNV%2520Tyagarajan&amp;source=gmail&amp;ust=1569582956994000&amp;usg=AFQjCNH12cEZ2dSUuG6nT_gxxydezBKJXw"><span style="font-family:&quot;Arial&quot;,sans-serif;text-decoration:none"><img border="0" width="60" height="60" style="width:.625in;height:.625in" id="m_-4625585253305646185_x0000_i1036" src="https://ci3.googleusercontent.com/proxy/pE5xT0NgDwF4OEQzGHxSRZv6JG30b52TP-P1z4iruqSTiKxwPc0UVnIE3eC12GOomEO2Wo-7BPBs86MgLaDCfTHSdYI5IgxSzcl3bAnRb_Np60-bg1fBNsVQLqhN3-w=s0-d-e1-ft#https://s3-us-west-2.amazonaws.com/xiqapp-static/Persons/tigertyagarajan.jpg" alt="cxo"></span></a><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			<td style="padding:0in 0in 0in 0in">
			<p class="m_-4625585253305646185cxo-name" style="line-height:15.75pt"><a href="http://xiqinc.app.link/?entity=person&amp;source=diq&amp;id=288400&amp;title=NV%20Tyagarajan" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Dperson%26source%3Ddiq%26id%3D288400%26title%3DNV%2520Tyagarajan&amp;source=gmail&amp;ust=1569582956994000&amp;usg=AFQjCNH12cEZ2dSUuG6nT_gxxydezBKJXw"><b><span style="font-size:13.5pt;color:#333333">NV Tyagarajan</span></b></a><b><span style="font-size:13.5pt"><u></u><u></u></span></b></p>
			<p class="MsoNormal"><span class="m_-4625585253305646185cxo-position"><span style="font-size:9.0pt;color:#8d8d8d">Chief Executive Officer &amp; President</span></span><span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#8d8d8d"><br>
			</span><span class="m_-4625585253305646185cxo-company"><b><span style="font-size:10.5pt">Genpact Ltd. </span>
			</b></span><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			</tbody>
			</table>
			</div>
			</td>
			<td width="50%" style="width:50.0%;padding:0in 22.5pt 37.5pt 6.0pt">
			<div align="center">
			<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;border-collapse:collapse">
			<tbody>
			<tr>
			<td width="80" style="width:60.0pt;padding:0in 0in 0in 0in">
			<p class="MsoNormal"><a href="http://xiqinc.app.link/?entity=person&amp;source=diq&amp;id=125990&amp;title=Kent%20Walker" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Dperson%26source%3Ddiq%26id%3D125990%26title%3DKent%2520Walker&amp;source=gmail&amp;ust=1569582956994000&amp;usg=AFQjCNFbB66H9PC3jhVtKel5bzhb41V9jg"><span style="font-family:&quot;Arial&quot;,sans-serif;text-decoration:none"><img border="0" width="60" height="60" style="width:.625in;height:.625in" id="m_-4625585253305646185_x0000_i1035" src="https://ci6.googleusercontent.com/proxy/vFbAe-Gpl5DKd-mhCXd3Vd6zUbf3Pt7MdzQ7L81NzOfWHTfAGcE0tVYuq3f7wERcJeneF7fEhm6rJYevEI-64Ew7qHI5vfCkmrzPzXgVTA=s0-d-e1-ft#https://api.xiq.io/static/admin/images/Executives/125990.jpg" alt="cxo"></span></a><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			<td style="padding:0in 0in 0in 0in">
			<p class="m_-4625585253305646185cxo-name" style="line-height:15.75pt"><a href="http://xiqinc.app.link/?entity=person&amp;source=diq&amp;id=125990&amp;title=Kent%20Walker" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Dperson%26source%3Ddiq%26id%3D125990%26title%3DKent%2520Walker&amp;source=gmail&amp;ust=1569582956994000&amp;usg=AFQjCNFbB66H9PC3jhVtKel5bzhb41V9jg"><b><span style="font-size:13.5pt;color:#333333">Kent Walker</span></b></a><b><span style="font-size:13.5pt"><u></u><u></u></span></b></p>
			<p class="MsoNormal"><span class="m_-4625585253305646185cxo-position"><span style="font-size:9.0pt;color:#8d8d8d">Senior Vice President and General Counsel, Global affair</span></span><span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#8d8d8d"><br>
			</span><span class="m_-4625585253305646185cxo-company"><b><span style="font-size:10.5pt">Google Inc.</span></b></span><span style="font-family:&quot;Arial&quot;,sans-serif">
			<u></u><u></u></span></p>
			</td>
			</tr>
			</tbody>
			</table>
			</div>
			</td>
			</tr>
			<tr>
			<td width="50%" style="width:50.0%;padding:0in 6.0pt 37.5pt 22.5pt">
			<div align="center">
			<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;border-collapse:collapse">
			<tbody>
			<tr>
			<td width="80" style="width:60.0pt;padding:0in 0in 0in 0in">
			<p class="MsoNormal"><a href="http://xiqinc.app.link/?entity=person&amp;source=diq&amp;id=288249&amp;title=Kevin%20Systrom" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Dperson%26source%3Ddiq%26id%3D288249%26title%3DKevin%2520Systrom&amp;source=gmail&amp;ust=1569582956994000&amp;usg=AFQjCNGcOmnnzvtxEDJQC2XHP1zpNbRrug"><span style="font-family:&quot;Arial&quot;,sans-serif;text-decoration:none"><img border="0" width="60" height="60" style="width:.625in;height:.625in" id="m_-4625585253305646185_x0000_i1034" src="https://ci6.googleusercontent.com/proxy/5W8ygly43ulljpppq213WgDP2TTTu5iv_RNMUNvc26MIkQ6K7P1CTXXt9-uYiBcMLJ_vyh-Y1nbVXFnyh3TW28046pKLN5E_8uRn_LZBEA=s0-d-e1-ft#https://api.xiq.io/static/admin/images/Executives/288249.jpg" alt="cxo"></span></a><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			<td style="padding:0in 0in 0in 0in">
			<p class="m_-4625585253305646185cxo-name" style="line-height:15.75pt"><a href="http://xiqinc.app.link/?entity=person&amp;source=diq&amp;id=288249&amp;title=Kevin%20Systrom" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Dperson%26source%3Ddiq%26id%3D288249%26title%3DKevin%2520Systrom&amp;source=gmail&amp;ust=1569582956994000&amp;usg=AFQjCNGcOmnnzvtxEDJQC2XHP1zpNbRrug"><b><span style="font-size:13.5pt;color:#333333">Kevin Systrom</span></b></a><b><span style="font-size:13.5pt"><u></u><u></u></span></b></p>
			<p class="MsoNormal"><span class="m_-4625585253305646185cxo-position"><span style="font-size:9.0pt;color:#8d8d8d">Co-founder</span></span><span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#8d8d8d"><br>
			</span><span class="m_-4625585253305646185cxo-company"><b><span style="font-size:10.5pt">Instagram from Facebook</span></b></span><span style="font-family:&quot;Arial&quot;,sans-serif">
			<u></u><u></u></span></p>
			</td>
			</tr>
			</tbody>
			</table>
			</div>
			</td>
			<td width="50%" style="width:50.0%;padding:0in 22.5pt 37.5pt 6.0pt">
			<div align="center">
			<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;border-collapse:collapse">
			<tbody>
			<tr>
			<td width="80" style="width:60.0pt;padding:0in 0in 0in 0in">
			<p class="MsoNormal"><a href="http://xiqinc.app.link/?entity=person&amp;source=diq&amp;id=288250&amp;title=Mike%20Krieger" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Dperson%26source%3Ddiq%26id%3D288250%26title%3DMike%2520Krieger&amp;source=gmail&amp;ust=1569582956995000&amp;usg=AFQjCNGgjPyaNADo-PIdUaO-drwY9lxPbQ"><span style="font-family:&quot;Arial&quot;,sans-serif;text-decoration:none"><img border="0" width="60" height="60" style="width:.625in;height:.625in" id="m_-4625585253305646185_x0000_i1033" src="https://ci6.googleusercontent.com/proxy/ZEOs2gWEDcgYoBKFEH9gESbP1ZCepwf--xLi5wIVXrQoFTdLIUKwDpDCWkum0FzmB0VPl8lK9Z_MAXCVry2qd55zC31-8fxJYg1BfR3PQQ=s0-d-e1-ft#https://api.xiq.io/static/admin/images/Executives/288250.jpg" alt="cxo"></span></a><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			<td style="padding:0in 0in 0in 0in">
			<p class="m_-4625585253305646185cxo-name" style="line-height:15.75pt"><a href="http://xiqinc.app.link/?entity=person&amp;source=diq&amp;id=288250&amp;title=Mike%20Krieger" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Dperson%26source%3Ddiq%26id%3D288250%26title%3DMike%2520Krieger&amp;source=gmail&amp;ust=1569582956995000&amp;usg=AFQjCNGgjPyaNADo-PIdUaO-drwY9lxPbQ"><b><span style="font-size:13.5pt;color:#333333">Mike Krieger</span></b></a><b><span style="font-size:13.5pt"><u></u><u></u></span></b></p>
			<p class="MsoNormal"><span class="m_-4625585253305646185cxo-position"><span style="font-size:9.0pt;color:#8d8d8d">Co-founder</span></span><span style="font-size:9.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#8d8d8d"><br>
			</span><span class="m_-4625585253305646185cxo-company"><b><span style="font-size:10.5pt">Instagram from Facebook</span></b></span><span style="font-family:&quot;Arial&quot;,sans-serif">
			<u></u><u></u></span></p>
			</td>
			</tr>
			</tbody>
			</table>
			</div>
			</td>
			</tr>
			<tr>
			<td colspan="2" style="padding:0in 0in 33.75pt 0in">
			<p class="MsoNormal" align="center" style="text-align:center"><a href="http://xiqinc.app.link/?entity=widget&amp;source=diq&amp;type=people&amp;category=Executives&amp;title=CxO%20Tweets" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://xiqinc.app.link/?entity%3Dwidget%26source%3Ddiq%26type%3Dpeople%26category%3DExecutives%26title%3DCxO%2520Tweets&amp;source=gmail&amp;ust=1569582956995000&amp;usg=AFQjCNHHOZkd3r_3CXMuH5hlKILywXJ97A"><span style="font-family:&quot;Arial&quot;,sans-serif;text-decoration:none"><img border="0" width="300" height="50" style="width:3.125in;height:.525in" id="m_-4625585253305646185_x0000_i1032" src="https://ci4.googleusercontent.com/proxy/mobp62pEfgtebCR20g64zARMIrSa7FJ5VqJJrPphgJxe_6lzn9scS_aVeeLu5-LMO5IfHo9UrH9E29RcjBoGfMRlT2MTk6_h42geSXUPzBz4Q74drw0CP99K-KuApCrqw7YiJhDMIA=s0-d-e1-ft#https://media.xiq.io/user_images/1563103315_96666a2e-a629-11e9-a98d-06b5fc41d42e.png" alt="https://media.xiq.io/user_images/1563103315_96666a2e-a629-11e9-a98d-06b5fc41d42e.png"></span></a><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			<tr>
			<td colspan="2" style="background:#edf1f5;padding:18.75pt 22.5pt 15.0pt 22.5pt">
			<p class="MsoNormal"><span style="font-size:8.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#61769e">Daily IQ is a email notification of the top stories and breaking news from the companies you selected in xiQ. To modify the selection you may change your My Account
			selection in xiQ. You are receiving this mail because you signed up to xiQ</span><span style="font-family:&quot;Arial&quot;,sans-serif">
			<u></u><u></u></span></p>
			</td>
			</tr>
			<tr>
			<td colspan="2" style="background:#edf1f5;padding:0in 22.5pt 15.0pt 22.5pt">
			<p class="MsoNormal" align="center" style="text-align:center"><a href="http://kbbm6lps.r.us-west-2.awstrack.me/L0/http:%2F%2Fworkbench.xiq.io%2Fworkbench%2Funsubscriber%2F%3Fdaily_alert_email_subscribe=1%26email=c3JpenZpQHhpcWluYy5jb20=%26campaign_id=013b4e3946ac4c3f8b3895c6f9fbbb8f%26contact_id=/1/0101016d68ab2c22-9fe2b45f-3943-452f-922c-118869233441-000000/cpPiOG0N1ijurasyyRlEvhZJaDA=129" title="Unsubscribe Here" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=http://kbbm6lps.r.us-west-2.awstrack.me/L0/http:%252F%252Fworkbench.xiq.io%252Fworkbench%252Funsubscriber%252F%253Fdaily_alert_email_subscribe%3D1%2526email%3Dc3JpenZpQHhpcWluYy5jb20%3D%2526campaign_id%3D013b4e3946ac4c3f8b3895c6f9fbbb8f%2526contact_id%3D/1/0101016d68ab2c22-9fe2b45f-3943-452f-922c-118869233441-000000/cpPiOG0N1ijurasyyRlEvhZJaDA%3D129&amp;source=gmail&amp;ust=1569582956995000&amp;usg=AFQjCNEy5Wf_hgkCKJM5e6zg1ZDzg8suyg"><b><span style="font-size:7.5pt;font-family:&quot;Arial&quot;,sans-serif;color:#e15869;text-decoration:none">Unsubscribe
			Here</span></b></a><span style="font-family:&quot;Arial&quot;,sans-serif"> <u></u><u></u></span></p>
			</td>
			</tr>
			<tr>
			<td colspan="2" style="background:#edf1f5;padding:0in 22.5pt 0in 22.5pt">
			<p class="m_-4625585253305646185download-title" align="center" style="margin-bottom:9.0pt;text-align:center;line-height:13.5pt">
			<b><span style="font-size:9.0pt;color:#61769e">Download xiQ Mobile App<u></u><u></u></span></b></p>
			<div align="center">
			<table border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100.0%;border-collapse:collapse">
			<tbody>
			<tr>
			<td width="50%" style="width:50.0%;padding:0in 6.0pt 0in 0in">
			<p class="MsoNormal" align="right" style="text-align:right"><a href="https://kbbm6lps.r.us-west-2.awstrack.me/L0/https:%2F%2Fitunes.apple.com%2Fus%2Fapp%2Fxiq%2Fid869245291%3Fmt=8/1/0101016d68ab2c22-9fe2b45f-3943-452f-922c-118869233441-000000/mhxR2YcM0hzoYNJ7MnzXDPt_kIw=129" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=https://kbbm6lps.r.us-west-2.awstrack.me/L0/https:%252F%252Fitunes.apple.com%252Fus%252Fapp%252Fxiq%252Fid869245291%253Fmt%3D8/1/0101016d68ab2c22-9fe2b45f-3943-452f-922c-118869233441-000000/mhxR2YcM0hzoYNJ7MnzXDPt_kIw%3D129&amp;source=gmail&amp;ust=1569582956995000&amp;usg=AFQjCNF5t_GXbSV8Yy96-cIJHuAz0mQN2A"><span style="font-family:&quot;Arial&quot;,sans-serif;text-decoration:none"><img border="0" width="133" height="42" style="width:1.3833in;height:.4416in" id="m_-4625585253305646185_x0000_i1031" src="https://ci6.googleusercontent.com/proxy/ARxT-uSTK_dgctrgJVEOrsmhX0hPmBAg3_MSPU7YVJNHzotWTIQxfE3Lvpv9Xjss5JuzGjgakPL94v9neCMUfzL3OfGtar15mt37dpn4WueWP3ZcrE0X6Akzu-qiR-KW8-0hgvumxg=s0-d-e1-ft#https://media.xiq.io/user_images/1561125349_4671cd60-942c-11e9-9695-06b5fc41d42e.png" alt="download app store"></span></a><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			<td width="50%" style="width:50.0%;padding:0in 0in 0in 6.0pt">
			<p class="MsoNormal"><a href="https://kbbm6lps.r.us-west-2.awstrack.me/L0/https:%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid=com.xiq.app%26hl=en/1/0101016d68ab2c22-9fe2b45f-3943-452f-922c-118869233441-000000/m0MgvEjrBlQ1tkUnd2Yt1-d_pQg=129" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=https://kbbm6lps.r.us-west-2.awstrack.me/L0/https:%252F%252Fplay.google.com%252Fstore%252Fapps%252Fdetails%253Fid%3Dcom.xiq.app%2526hl%3Den/1/0101016d68ab2c22-9fe2b45f-3943-452f-922c-118869233441-000000/m0MgvEjrBlQ1tkUnd2Yt1-d_pQg%3D129&amp;source=gmail&amp;ust=1569582956995000&amp;usg=AFQjCNH6PvMbHxtLlClksXps_R41MBH7fg"><span style="font-family:&quot;Arial&quot;,sans-serif;text-decoration:none"><img border="0" width="140" height="42" style="width:1.4583in;height:.4416in" id="m_-4625585253305646185_x0000_i1030" src="https://ci5.googleusercontent.com/proxy/XvBNqY8M-_0KhF7AuxebpaiS4mLFvgUrnZnzogC7OXaGD2sv0rzs_-W_x8SIebNtffgE78wpdePLMUsyamxXiA-tLV2wEIfx95vCQtBeTNPzTG3cq0VpyC7m-Uwi3_-kFZSlgk1DYw=s0-d-e1-ft#https://media.xiq.io/user_images/1561123527_084dbe08-9428-11e9-8f48-06b5fc41d42e.png" alt="download app store"></span></a><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			</tbody>
			</table>
			</div>
			</td>
			</tr>
			<tr>
			<td colspan="2" style="background:#edf1f5;padding:11.25pt 22.5pt 11.25pt 22.5pt">
			<p align="center" style="text-align:center;line-height:13.5pt"><span style="font-size:9.0pt;color:#61769e">100 Redwood Shores Parkway, Suite 100 Redwood City, CA 94065, USA<u></u><u></u></span></p>
			</td>
			</tr>
			<tr>
			<td colspan="2" style="background:#edf1f5;padding:0in 22.5pt 22.5pt 22.5pt">
			<div align="center">
			<table border="0" cellspacing="0" cellpadding="0" width="160" style="width:120.0pt;border-collapse:collapse">
			<tbody>
			<tr>
			<td style="padding:0in 3.75pt 0in 3.75pt">
			<p class="MsoNormal" align="center" style="text-align:center"><a href="https://kbbm6lps.r.us-west-2.awstrack.me/L0/https:%2F%2Fwww.facebook.com%2Fxiqai%2F/1/0101016d68ab2c22-9fe2b45f-3943-452f-922c-118869233441-000000/f1xHPMeAYwA7X_pod2pdoUa0g54=129" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=https://kbbm6lps.r.us-west-2.awstrack.me/L0/https:%252F%252Fwww.facebook.com%252Fxiqai%252F/1/0101016d68ab2c22-9fe2b45f-3943-452f-922c-118869233441-000000/f1xHPMeAYwA7X_pod2pdoUa0g54%3D129&amp;source=gmail&amp;ust=1569582956995000&amp;usg=AFQjCNFUcjmYQs_ZsoAeBYAEe3ww3dvTYQ"><span style="font-family:&quot;Arial&quot;,sans-serif;text-decoration:none"><img border="0" width="25" height="25" style="width:.2583in;height:.2583in" id="m_-4625585253305646185_x0000_i1029" src="https://ci5.googleusercontent.com/proxy/TfKPQZQhKp3FWs8rKab0Pd0RMoSAdxgvRXrv7X5r7GO_PfdS6Tw2m8vSZN5q4qiQYiCaA30MqfvG4oYNgsxIjEPn2c2QGzztz5My2S8AhBD09sKvl3XKlmXHrRwzn5OBvh2de0rGvg=s0-d-e1-ft#https://media.xiq.io/user_images/1561123905_e9d59b0c-9428-11e9-a7ed-06b5fc41d42e.png" alt="fb"></span></a><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			<td style="padding:0in 3.75pt 0in 3.75pt">
			<p class="MsoNormal" align="center" style="text-align:center"><a href="https://kbbm6lps.r.us-west-2.awstrack.me/L0/https:%2F%2Ftwitter.com%2Fxiqinc/1/0101016d68ab2c22-9fe2b45f-3943-452f-922c-118869233441-000000/ELq36cDYgj2d0KH5VEVaVbuRSsw=129" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=https://kbbm6lps.r.us-west-2.awstrack.me/L0/https:%252F%252Ftwitter.com%252Fxiqinc/1/0101016d68ab2c22-9fe2b45f-3943-452f-922c-118869233441-000000/ELq36cDYgj2d0KH5VEVaVbuRSsw%3D129&amp;source=gmail&amp;ust=1569582956995000&amp;usg=AFQjCNH_7spYuylMdKXnM3MQ6zprG_SEuw"><span style="font-family:&quot;Arial&quot;,sans-serif;text-decoration:none"><img border="0" width="25" height="25" style="width:.2583in;height:.2583in" id="m_-4625585253305646185_x0000_i1028" src="https://ci6.googleusercontent.com/proxy/Qztc3SqBW0ulEC3sYnfu5ZM9082yLA5cSltD8bLtJGNDBkeWtJRHWhUenzm2sjRgflr0sdbjRtGdd98jXq_mQBRZ06uqLIOubQ-hVnQg-GAhvKxyraV0qGBEAbuKvmI4mKqo2JtxvQ=s0-d-e1-ft#https://media.xiq.io/user_images/1561125208_f29e88e0-942b-11e9-a2be-06b5fc41d42e.png" alt="twitter"></span></a><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			<td style="padding:0in 3.75pt 0in 3.75pt">
			<p class="MsoNormal" align="center" style="text-align:center"><a href="https://kbbm6lps.r.us-west-2.awstrack.me/L0/https:%2F%2Fwww.linkedin.com%2Fcompany%2Fxiqinc%2F/1/0101016d68ab2c22-9fe2b45f-3943-452f-922c-118869233441-000000/bUEIZz3oPFNJPV6xaJCeNn31KT0=129" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=https://kbbm6lps.r.us-west-2.awstrack.me/L0/https:%252F%252Fwww.linkedin.com%252Fcompany%252Fxiqinc%252F/1/0101016d68ab2c22-9fe2b45f-3943-452f-922c-118869233441-000000/bUEIZz3oPFNJPV6xaJCeNn31KT0%3D129&amp;source=gmail&amp;ust=1569582956995000&amp;usg=AFQjCNGMqLXxoQOlmY3yklhmr9GE4PRr3g"><span style="font-family:&quot;Arial&quot;,sans-serif;text-decoration:none"><img border="0" width="25" height="25" style="width:.2583in;height:.2583in" id="m_-4625585253305646185_x0000_i1027" src="https://ci4.googleusercontent.com/proxy/jNf55A1jaG0L6skv3nuxZdNwHPo5MguFpu9dBlaQAZGU6E1_nG29IZ69NU37sLzSodKjxGIvVOSkUN6-YudKSOEnycuyixWYAFKolzqCTyGc1a-fqrHTBcm1SCydivNKogkoONUC6g=s0-d-e1-ft#https://media.xiq.io/user_images/1561125255_0e9d74f2-942c-11e9-a2be-06b5fc41d42e.png" alt="linkedin"></span></a><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			<td style="padding:0in 3.75pt 0in 3.75pt">
			<p class="MsoNormal" align="center" style="text-align:center"><a href="https://kbbm6lps.r.us-west-2.awstrack.me/L0/https:%2F%2Fwww.youtube.com%2Fchannel%2FUC_l-CzKZavSriBrQyUQ-jVQ/1/0101016d68ab2c22-9fe2b45f-3943-452f-922c-118869233441-000000/LY8kM8lly_p_pvCcEHgs8wyNAOk=129" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en-GB&amp;q=https://kbbm6lps.r.us-west-2.awstrack.me/L0/https:%252F%252Fwww.youtube.com%252Fchannel%252FUC_l-CzKZavSriBrQyUQ-jVQ/1/0101016d68ab2c22-9fe2b45f-3943-452f-922c-118869233441-000000/LY8kM8lly_p_pvCcEHgs8wyNAOk%3D129&amp;source=gmail&amp;ust=1569582956996000&amp;usg=AFQjCNHBiKFIZDWkuX81mBD5sIocfNDkxA"><span style="font-family:&quot;Arial&quot;,sans-serif;text-decoration:none"><img border="0" width="25" height="25" style="width:.2583in;height:.2583in" id="m_-4625585253305646185_x0000_i1026" src="https://ci6.googleusercontent.com/proxy/2RwwmFnYivkcSdQBk4tm1ra_B4UgYThhTJZehdDfR5YAqCgc2L1IGTZVVcTzUbID42L6JBmYuRaL0oDCGjIUBsVGdnNa9Nnqhrqi_EJ91q4IU6qWtUgPlBlOU7MaVtq9sAMd_9eWRA=s0-d-e1-ft#https://media.xiq.io/user_images/1561123951_05087f8e-9429-11e9-a2be-06b5fc41d42e.png" alt="youtube"></span></a><span style="font-family:&quot;Arial&quot;,sans-serif"><u></u><u></u></span></p>
			</td>
			</tr>
			</tbody>
			</table>
			</div>
			</td>
			</tr>
			<tr>
			<td colspan="2" style="padding:7.5pt 0in 7.5pt 0in">
			<p class="m_-4625585253305646185copyright-top" align="center" style="margin-bottom:11.25pt;text-align:center;line-height:13.5pt">
			<span style="font-size:9.0pt;color:#b5c3d4">© Copyright xiQ Inc. 2019<u></u><u></u></span></p>
			</td>
			</tr>
			</tbody>
			</table>
		</div>
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


################# add attachment to the email ########################
ATTACHMENT = "C:\\Users\\srizvi\\Desktop\\reputation.jpg"
att = MIMEApplication(open(ATTACHMENT, 'rb').read())

# Add a header to tell the email client to treat this part as an attachment,
# and to give the attachment a name.
att.add_header('Content-Disposition','attachment',filename=os.path.basename(ATTACHMENT))

# Attach the multipart/alternative child container to the multipart/mixed
# parent container.
#msg.attach(msg_body)

# Add the attachment to the parent container.
msg.attach(att)
#############################################


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
