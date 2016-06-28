# -*-coding:utf-8-*=
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')
from util.iosutil import remotedriver
from time import sleep
from util.analysize_nodes import find_nodes
from util.analysize_nodes import get_nodes_config
from util.analysize_nodes import get_window_first_8_elements
from hashlib import md5


def traversal(dr, level):
	# store window id
	work_stacks = []
	repeat_pages = {
		'md5': 'count'
	}
	try:
		while work_stacks is []:
			xml_res = dr.page_source
			current_window_id = create_current_window_id(xml_res)
		res = True
	except:
		res = False
	finally:
		return res


def create_current_window_id(xml_res):
	window_string = get_window_first_8_elements(xml_res.encode('utf8'))
	window_id = create_md5(window_string.encode('utf8'))
	return window_id


def create_md5(window):
	m = md5()
	m.update(window)
	return m.hexdigest()


def get_current_page_all_nodes(xml_res):
	# get all nodes in current page
	click_config, input_config = get_nodes_config(filename='./node.xml')
	click_nodes, input_nodes = find_nodes(
		xml_res=xml_res.encode('utf8'),
		click_config=click_config,
		input_config=input_config
	)
	return click_nodes, input_nodes


if __name__ == '__main__':
	driver = remotedriver(bundle_id='com.gemd.iting', device_type='iPhone 5', ios_version='9.3.2')
	sleep(10)
	w_id = create_current_window_id(driver)
	sleep(10)
	driver.quit()
	print w_id