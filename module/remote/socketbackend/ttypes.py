#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autogenerated by pyload
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING

class BaseObject(object):
	__slots__ = []

class DownloadStatus:
	Aborted = 12
	Custom = 15
	Decrypting = 13
	Downloading = 10
	Failed = 7
	Finished = 5
	NA = 0
	Offline = 1
	Online = 2
	Paused = 4
	Processing = 14
	Queued = 3
	Skipped = 6
	Starting = 8
	TempOffline = 11
	Unknown = 16
	Waiting = 9

class FileStatus:
	Missing = 1
	Ok = 0
	Remote = 2

class Input:
	Bool = 4
	Choice = 6
	Click = 5
	List = 8
	Multiple = 7
	NA = 0
	Password = 3
	Table = 9
	Text = 1
	TextBox = 2

class MediaType:
	All = 0
	Archive = 32
	Audio = 2
	Document = 16
	Image = 4
	Other = 1
	Video = 8

class Output:
	All = 0
	Captcha = 2
	Notification = 1
	Query = 4

class PackageStatus:
	Ok = 0
	Paused = 1
	Remote = 2

class AccountInfo(BaseObject):
	__slots__ = ['plugin', 'loginname', 'valid', 'validuntil', 'trafficleft', 'maxtraffic', 'premium', 'activated', 'options']

	def __init__(self, plugin=None, loginname=None, valid=None, validuntil=None, trafficleft=None, maxtraffic=None, premium=None, activated=None, options=None):
		self.plugin = plugin
		self.loginname = loginname
		self.valid = valid
		self.validuntil = validuntil
		self.trafficleft = trafficleft
		self.maxtraffic = maxtraffic
		self.premium = premium
		self.activated = activated
		self.options = options

class AddonInfo(BaseObject):
	__slots__ = ['func_name', 'description', 'value']

	def __init__(self, func_name=None, description=None, value=None):
		self.func_name = func_name
		self.description = description
		self.value = value

class AddonService(BaseObject):
	__slots__ = ['func_name', 'description', 'media', 'package']

	def __init__(self, func_name=None, description=None, media=None, package=None):
		self.func_name = func_name
		self.description = description
		self.media = media
		self.package = package

class ConfigItem(BaseObject):
	__slots__ = ['name', 'display_name', 'description', 'type', 'default_value', 'value']

	def __init__(self, name=None, display_name=None, description=None, type=None, default_value=None, value=None):
		self.name = name
		self.display_name = display_name
		self.description = description
		self.type = type
		self.default_value = default_value
		self.value = value

class ConfigSection(BaseObject):
	__slots__ = ['name', 'display_name', 'description', 'long_description', 'items', 'info', 'handler']

	def __init__(self, name=None, display_name=None, description=None, long_description=None, items=None, info=None, handler=None):
		self.name = name
		self.display_name = display_name
		self.description = description
		self.long_description = long_description
		self.items = items
		self.info = info
		self.handler = handler

class DownloadInfo(BaseObject):
	__slots__ = ['url', 'plugin', 'hash', 'status', 'statusmsg', 'error']

	def __init__(self, url=None, plugin=None, hash=None, status=None, statusmsg=None, error=None):
		self.url = url
		self.plugin = plugin
		self.hash = hash
		self.status = status
		self.statusmsg = statusmsg
		self.error = error

class EventInfo(BaseObject):
	__slots__ = ['eventname', 'event_args']

	def __init__(self, eventname=None, event_args=None):
		self.eventname = eventname
		self.event_args = event_args

class FileDoesNotExists(Exception):
	__slots__ = ['fid']

	def __init__(self, fid=None):
		self.fid = fid

class FileInfo(BaseObject):
	__slots__ = ['fid', 'name', 'package', 'size', 'status', 'media', 'added', 'fileorder', 'download']

	def __init__(self, fid=None, name=None, package=None, size=None, status=None, media=None, added=None, fileorder=None, download=None):
		self.fid = fid
		self.name = name
		self.package = package
		self.size = size
		self.status = status
		self.media = media
		self.added = added
		self.fileorder = fileorder
		self.download = download

class InteractionTask(BaseObject):
	__slots__ = ['iid', 'input', 'data', 'output', 'default_value', 'title', 'description', 'plugin']

	def __init__(self, iid=None, input=None, data=None, output=None, default_value=None, title=None, description=None, plugin=None):
		self.iid = iid
		self.input = input
		self.data = data
		self.output = output
		self.default_value = default_value
		self.title = title
		self.description = description
		self.plugin = plugin

class LinkStatus(BaseObject):
	__slots__ = ['url', 'name', 'plugin', 'size', 'status', 'packagename']

	def __init__(self, url=None, name=None, plugin=None, size=None, status=None, packagename=None):
		self.url = url
		self.name = name
		self.plugin = plugin
		self.size = size
		self.status = status
		self.packagename = packagename

class OnlineCheck(BaseObject):
	__slots__ = ['rid', 'data']

	def __init__(self, rid=None, data=None):
		self.rid = rid
		self.data = data

class PackageDoesNotExists(Exception):
	__slots__ = ['pid']

	def __init__(self, pid=None):
		self.pid = pid

class PackageInfo(BaseObject):
	__slots__ = ['pid', 'name', 'folder', 'root', 'site', 'comment', 'password', 'added', 'status', 'packageorder', 'stats', 'fids', 'pids']

	def __init__(self, pid=None, name=None, folder=None, root=None, site=None, comment=None, password=None, added=None, status=None, packageorder=None, stats=None, fids=None, pids=None):
		self.pid = pid
		self.name = name
		self.folder = folder
		self.root = root
		self.site = site
		self.comment = comment
		self.password = password
		self.added = added
		self.status = status
		self.packageorder = packageorder
		self.stats = stats
		self.fids = fids
		self.pids = pids

class PackageStats(BaseObject):
	__slots__ = ['linkstotal', 'linksdone', 'sizetotal', 'sizedone']

	def __init__(self, linkstotal=None, linksdone=None, sizetotal=None, sizedone=None):
		self.linkstotal = linkstotal
		self.linksdone = linksdone
		self.sizetotal = sizetotal
		self.sizedone = sizedone

class PackageView(BaseObject):
	__slots__ = ['root', 'files', 'packages']

	def __init__(self, root=None, files=None, packages=None):
		self.root = root
		self.files = files
		self.packages = packages

class ProgressInfo(BaseObject):
	__slots__ = ['fid', 'name', 'speed', 'eta', 'format_eta', 'bleft', 'size', 'format_size', 'percent', 'status', 'statusmsg', 'format_wait', 'wait_until', 'packageID', 'packageName', 'plugin']

	def __init__(self, fid=None, name=None, speed=None, eta=None, format_eta=None, bleft=None, size=None, format_size=None, percent=None, status=None, statusmsg=None, format_wait=None, wait_until=None, packageID=None, packageName=None, plugin=None):
		self.fid = fid
		self.name = name
		self.speed = speed
		self.eta = eta
		self.format_eta = format_eta
		self.bleft = bleft
		self.size = size
		self.format_size = format_size
		self.percent = percent
		self.status = status
		self.statusmsg = statusmsg
		self.format_wait = format_wait
		self.wait_until = wait_until
		self.packageID = packageID
		self.packageName = packageName
		self.plugin = plugin

class ServerStatus(BaseObject):
	__slots__ = ['pause', 'active', 'queue', 'total', 'speed', 'download', 'reconnect']

	def __init__(self, pause=None, active=None, queue=None, total=None, speed=None, download=None, reconnect=None):
		self.pause = pause
		self.active = active
		self.queue = queue
		self.total = total
		self.speed = speed
		self.download = download
		self.reconnect = reconnect

class ServiceDoesNotExists(Exception):
	__slots__ = ['plugin', 'func']

	def __init__(self, plugin=None, func=None):
		self.plugin = plugin
		self.func = func

class ServiceException(Exception):
	__slots__ = ['msg']

	def __init__(self, msg=None):
		self.msg = msg

class UserData(BaseObject):
	__slots__ = ['name', 'email', 'role', 'permission', 'templateName']

	def __init__(self, name=None, email=None, role=None, permission=None, templateName=None):
		self.name = name
		self.email = email
		self.role = role
		self.permission = permission
		self.templateName = templateName

class UserDoesNotExists(Exception):
	__slots__ = ['user']

	def __init__(self, user=None):
		self.user = user

class Iface:
	def addFromCollector(self, name, paused):
		pass
	def addLinks(self, pid, links):
		pass
	def addPackage(self, name, links, password):
		pass
	def addPackageChild(self, name, links, password, root, paused):
		pass
	def addPackageP(self, name, links, password, paused):
		pass
	def addToCollector(self, links):
		pass
	def autoAddLinks(self, links):
		pass
	def call(self, plugin, func, arguments):
		pass
	def callAddonHandler(self, plugin, func, pid_or_fid):
		pass
	def checkOnlineStatus(self, urls):
		pass
	def checkOnlineStatusContainer(self, urls, filename, data):
		pass
	def checkURLs(self, urls):
		pass
	def configureSection(self, section):
		pass
	def createPackage(self, name, folder, root, password, site, comment, paused):
		pass
	def deleteCollLink(self, url):
		pass
	def deleteCollPack(self, name):
		pass
	def deleteFiles(self, fids):
		pass
	def deletePackages(self, pids):
		pass
	def findFiles(self, pattern):
		pass
	def freeSpace(self):
		pass
	def generateAndAddPackages(self, links, paused):
		pass
	def generateDownloadLink(self, fid, timeout):
		pass
	def generatePackages(self, links):
		pass
	def getAccountTypes(self):
		pass
	def getAccounts(self, refresh):
		pass
	def getAddonHandler(self):
		pass
	def getAllFiles(self):
		pass
	def getAllInfo(self):
		pass
	def getAllUnfinishedFiles(self):
		pass
	def getAllUserData(self):
		pass
	def getCollector(self):
		pass
	def getConfig(self):
		pass
	def getConfigValue(self, section, option):
		pass
	def getEvents(self, uuid):
		pass
	def getFileInfo(self, fid):
		pass
	def getFileTree(self, pid, full):
		pass
	def getInfoByPlugin(self, plugin):
		pass
	def getInteractionTask(self, mode):
		pass
	def getLog(self, offset):
		pass
	def getNotifications(self):
		pass
	def getPackageContent(self, pid):
		pass
	def getPackageInfo(self, pid):
		pass
	def getPluginConfig(self):
		pass
	def getProgressInfo(self):
		pass
	def getServerVersion(self):
		pass
	def getServices(self):
		pass
	def getUnfinishedFileTree(self, pid, full):
		pass
	def getUserData(self, username, password):
		pass
	def hasService(self, plugin, func):
		pass
	def isInteractionWaiting(self, mode):
		pass
	def isTimeDownload(self):
		pass
	def isTimeReconnect(self):
		pass
	def kill(self):
		pass
	def login(self, username, password):
		pass
	def moveFiles(self, fids, pid):
		pass
	def movePackage(self, pid, root):
		pass
	def orderFiles(self, fids, pid, position):
		pass
	def orderPackage(self, pids, position):
		pass
	def parseURLs(self, html, url):
		pass
	def pauseServer(self):
		pass
	def pollResults(self, rid):
		pass
	def recheckPackage(self, pid):
		pass
	def removeAccount(self, plugin, account):
		pass
	def renameCollPack(self, name, new_name):
		pass
	def restart(self):
		pass
	def restartFailed(self):
		pass
	def restartFile(self, fid):
		pass
	def restartPackage(self, pid):
		pass
	def scanDownloadFolder(self):
		pass
	def setConfigHandler(self, plugin, iid, value):
		pass
	def setConfigValue(self, section, option, value):
		pass
	def setFilePaused(self, fid, paused):
		pass
	def setInteractionResult(self, iid, result):
		pass
	def setPackageData(self, pid, data):
		pass
	def setPackageFolder(self, pid, path):
		pass
	def setPackagePaused(self, pid, paused):
		pass
	def statusServer(self):
		pass
	def stopAllDownloads(self):
		pass
	def stopDownloads(self, fids):
		pass
	def togglePause(self):
		pass
	def toggleReconnect(self):
		pass
	def unpauseServer(self):
		pass
	def updateAccount(self, plugin, account, password, options):
		pass
	def uploadContainer(self, filename, data):
		pass

