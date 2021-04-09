# -*- encoding : utf-8 -*-
import pandas as pd
from utils import emailUtils
def emailFormat(content):

    d = ""
    print(content)
    for i in range(len(content)):
        d = d + """
            <tr>
              <td align="center"><a href="http://10.10.12.47/zentao/bug-view-"""+str(content[i]["id"])+""".html"> """+ str(content[i]["id"]) + """</a></td>
              <td width="50%" align="left">""" + str(content[i]["title"]) + """</td>
              <td align="center">""" + str(content[i]['severity']) + """</td>
              <td align="center">""" + str(content[i]['assignedTo']) + """</td>
              <td align="center"> <font color="#FF0000">""" + str(content[i]['outDate']) + """</font> </td>
              
            </tr>
            """

    html = """
        <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <body>
    <div id="container">
    <p><strong>超期Bug未处理列表如下:</strong></p>
    <div id="content">
     <table width="90%" border="1" bordercolor="black" cellspacing="0" cellpadding="0">
    <tr>
      <td align="center"><strong>BugId</strong></td>
      <td align="center"><strong>描述</strong></td>
      <td align="center"><strong>严重等级</strong></td>
      <td align="center"><strong>当前人员</strong></td>
      <td align="center" color="red"><strong>超期（天数）</strong></td>
    </tr>""" + d + """
    </table>
    </div>
    </div>
    </div>
    </body>
    </html>
    """


    emailUtils.emailConf().sendMail(html)
