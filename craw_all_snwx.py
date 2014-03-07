#encoding=utf8

import sys,urllib2,sgmllib,os
url="";


class showStructure(sgmllib.SGMLParser):
	def __init__(self):
		self.infotitle_flag = 0;
		self.intro_flag = 0;
		self.text_flag = 0;
		self.intro = "";
		self.text = "";
		self.split_tag = "：";
		sgmllib.SGMLParser.__init__(self)  
	
	def start_div(self, attrs):
		for k,v in attrs:
			if(k=="class" and v=="infotitle"):
				self.infotitle_flag = 1;
				break;
			if(k=="class" and v=="intro"):
				self.intro_flag = 1
				break;
			if(k=="id" and v == "list"):
				self.text_flag   = 1;
				break;
	def end_div(self):
		self.infotitle_flag = 0;
		self.intro_flag = 0;
		self.text_flag = 0;
	def handle_data(self, text):
		if(self.infotitle_flag == 1):
			content = text.split(self.split_tag);
			print len(content);
			if(len(content) == 1):
				self.title = text;
			elif(content[0]=="作者"):
				self.author = content[1];
			elif(content[0]=="类别"):
				self.leibie = content[1];
			elif(content[0]=="状态"):
				self.status = content[1];
		if(self.intro_flag == 1):
			self.intro += text;
		if(self.text_flag == 1):wq

:
			self.text += text;
			



if __name__ == "__main__":

	dir_id = 0;
	xs_id = 0;

	for xs_id in range(0,100):
		dir_id = xs_id/1000;
		url = "http://www.snwx.com/book/%d/%d/" % (dir_id, xs_id);
		fd=urllib2.urlopen(url);
		content = fd.read();
		type = sys.getfilesystemencoding()      # local encode format  
		content = content.decode("gbk").encode(type)  # convert encode format
		xiaoshuo_info = showStructure();
		xiaoshuo_info.feed(content);
		print xiaoshuo_info.text;
		print xiaoshuo_info.author;
		print xiaoshuo_info.title;
		fd.close();
