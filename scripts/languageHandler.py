import __builtin__
import os
import sys
import ctypes
import locale
import gettext
#import paths
import platform

# A fix for the mac locales
if platform.system() != 'Windows':
 if locale.getlocale()[0] is None:
  locale.setlocale(locale.LC_ALL, 'en_US')

#a few Windows locale constants
LOCALE_SLANGUAGE=0x2
LOCALE_SLANGDISPLAYNAME=0x6f

curLang="en"

def localeNameToWindowsLCID(localeName):
	"""Retreave the Windows locale identifier (LCID) for the given locale name
	@param localeName: a string of 2letterLanguage_2letterCountry or or just 2letterLanguage
	@type localeName: string
	@returns: a Windows LCID
	@rtype: integer
	""" 
	#Windows Vista is able to convert locale names to LCIDs
	func_LocaleNameToLCID=getattr(ctypes.windll.kernel32,'LocaleNameToLCID',None)
	if func_LocaleNameToLCID is not None:
		localeName=localeName.replace('_','-')
		LCID=func_LocaleNameToLCID(unicode(localeName),0)
	else: #Windows doesn't have this functionality, manually search Python's windows_locale dictionary for the LCID
		localeName=locale.normalize(localeName)
		if '.' in localeName:
			localeName=localeName.split('.')[0]
		LCList=[x[0] for x in locale.windows_locale.iteritems() if x[1]==localeName]
		if len(LCList)>0:
			LCID=LCList[0]
		else:
			LCID=0
	return LCID

def getLanguageDescription(language):
	"""Finds out the description (localized full name) of a given local name"""
	desc=None
	if platform.system() == "Windows":
		LCID=localeNameToWindowsLCID(language)
		if LCID!=0:
			buf=ctypes.create_unicode_buffer(1024)
			if '_' not in language:
				res=ctypes.windll.kernel32.GetLocaleInfoW(LCID,LOCALE_SLANGDISPLAYNAME,buf,1024)
			else:
				res=0
			if res==0:
				res=ctypes.windll.kernel32.GetLocaleInfoW(LCID,LOCALE_SLANGUAGE,buf,1024)
			desc=buf.value
	elif platform.system() == "Linux" or not desc:
		desc={
			"am":pgettext("languageName","Amharic"),
			"an":pgettext("languageName","Aragonese"),
			"es":pgettext("languageName","Spanish"),
			"pt":pgettext("languageName","Portuguese"),
			"ru":pgettext("languageName","Russian"),
			"it":pgettext("languageName","italian"),
			"tr":pgettext("languageName","Turkey"),
			"gl":pgettext("languageName","Galician"),
			"ca":pgettext("languageName","Catala"),
			"eu":pgettext("languageName","Vasque"),
			"pl":pgettext("languageName","polish"),
			"ar":pgettext("languageName","Arabic"),
			"ne":pgettext("languageName","Nepali"),
			"sr":pgettext("languageName","Serbian (Latin)"),
		}.get(language,None)
	return desc

def getAvailableLanguages():
	"""generates a list of locale names, plus their full localized language and country names.
	@rtype: list of tuples
	"""
	#Make a list of all the locales found in NVDA's locale dir
	l=[x for x in os.listdir("locales") if not x.startswith('.')]
	l=[x for x in l if os.path.isfile('locales/%s/LC_MESSAGES/twblue-documentation.mo' % x)]
	#Make sure that en (english) is in the list as it may not have any locale files, but is default
	if 'en' not in l:
		l.append('en')
		l.sort()
	#For each locale, ask Windows for its human readable display name
	d=[]
	for i in l:
		desc=getLanguageDescription(i)
		label="%s, %s"%(desc,i) if desc else i
		d.append(label)
	#include a 'user default, windows' language, which just represents the default language for this user account
	l.append("system")
	# Translators: the label for the Windows default NVDA interface language.
	d.append(_("User default"))
	#return a zipped up version of both the lists (a list with tuples of locale,label)
	return zip(l,d)

def makePgettext(translations):
	"""Obtaina  pgettext function for use with a gettext translations instance.
	pgettext is used to support message contexts,
	but Python 2.7's gettext module doesn't support this,
	so NVDA must provide its own implementation.
	"""
	if isinstance(translations, gettext.GNUTranslations):
		def pgettext(context, message):
			message = unicode(message)
			try:
				# Look up the message with its context.
				return translations._catalog[u"%s\x04%s" % (context, message)]
			except KeyError:
				return message
	else:
		def pgettext(context, message):
			return unicode(message)
	return pgettext

def setLanguage(lang, translation_file=""):
	system = platform.system()
	global curLang
	try:
		if lang=="system":
			if system == "Windows":
				windowsLCID=ctypes.windll.kernel32.GetUserDefaultUILanguage()
				localeName=locale.windows_locale[windowsLCID]
			else:
				localeName=locale.getlocale()[0]
			trans=gettext.translation(translation_file, localedir="../translations", languages=[localeName])
			curLang=localeName
		else:
			trans=gettext.translation(translation_file, localedir="../translations", languages=[lang])
			curLang=lang
			localeChanged=False
			#Try setting Python's locale to lang
			try:
				locale.setlocale(locale.LC_ALL, lang)
				localeChanged=True
			except:
				pass
			if not localeChanged and '_' in lang:
				#Python couldn'tsupport the language_country locale, just try language.
				try:
					locale.setlocale(locale.LC_ALL, lang.split('_')[0])
				except:
					pass
			#Set the windows locale for this thread (NVDA core) to this locale.
			if system == "Windows":
				LCID=localeNameToWindowsLCID(lang)
				ctypes.windll.kernel32.SetThreadLocale(LCID)
	except IOError:
		trans=gettext.translation(translation_file,fallback=True)
		curLang="en"
	trans.install(unicode=True)
	# Install our pgettext function.
	__builtin__.__dict__["pgettext"] = makePgettext(trans)

def getLanguage():
	return curLang

def normalizeLanguage(lang):
	"""
	Normalizes a  language-dialect string  in to a standard form we can deal with.
	Converts  any dash to underline, and makes sure that language is lowercase and dialect is upercase.
	"""
	lang=lang.replace('-','_')
	ld=lang.split('_')
	ld[0]=ld[0].lower()
	#Filter out meta languages such as x-western
	if ld[0]=='x':
		return None
	if len(ld)>=2:
		ld[1]=ld[1].upper()
	return "_".join(ld)

