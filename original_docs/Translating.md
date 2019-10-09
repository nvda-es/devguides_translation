# NVDA Translation and Localization

Thank you for considering to localize NVDA to your language, or improving an existing translation.
In order to support multiple languages/locales, NVDA must be translated and data specific to the locale must be provided.
There are several tasks to be done, and this document hopes to give you an overview and guide you through the process.


## Translation Mailing List
Translators should subscribe to the [NVDA translations mailing list](https://groups.io/g/nvda-translations)
hosted at Groups.IO.

It is an English low trafic list devoted for the discussion of translation. 
Important messages that relate to translators will also be sent here, i.e. before official NVDA releases, to remind translators to make sure their localization is up to date.

## Important Dates

Translators should ensure their translation is up to date by (UTC 00:00 on 14 February, 14 May, 14 August and 14 November) in order for it to be included in the upcoming final release, with this being delayed up to three days for some releases. Work submitted after this time will not be included in the upcoming release.  A reminder will be sent three to five days prior to end of this period. For further information please see the ReleaseProcess page.

## Translation Status

Status for existing NVDA localizations are provided below. If you would like to improve or would like to work on a new language, please write to the NVDA translations email list.
Information updated as of September 2019 (2019.2).
When 2019.2 is listed in the last updated column, it means that the localization is fully up to date and will be ready for the next release. For the purposes of the information below, "up to date" refers to interface translation of at least 90%.

| Language | Status | Last updated |
|------------|----------|----------------|
| af_ZA: Afrikaans | Not complete/out of date, maintainer needed. | Oct 2009 |
| am: Amharic | Not complete/out of date, maintainer needed. | Jul 2012 |
| an: Aragonese | nearly complete. | 2019.2 |
| ar: Arabic | Up to date. | 2019.2 |
| bg: Bulgarian | Up to date. | 2019.2 |
| CA: Catalan | not complete. | 2018.4 |
| CKB: Central Kurdish | Not complete/out of date, maintainer needed. | n.a. |
| cs: Czech | Documentation incomplete from Sept 2017. The NVDA interface is Up to date. | 2019.2 | 
| da: Danish | Up to date. | 2019.2 | 
| de: German | Up to date. | 2019.2 | 
| de_CH: Swiss German | Not complete/out of date, maintainer needed. | 2018.3 | 
| el: Greek | The NVDA interface is nearly complete. Documentation is out of date from Nov 2017| 2019.1 |
| es: Spanish | Up to date. | 2019.1 | 
| es_CO: Spanish (Columbia) | Not complete/out of date, maintainer needed. | Jul 2016|
| fa: Farsi | Up to date. | 2019.2 |
| fi: Finnish | Up to date. | 2019.2 | 
| fr: French | Up to date. | 2019.2 | 
| ga: Gaeilge (Ireland) | Interface: work in progress. | Dez 2018 |
| gl: Galician | Up to date. | 2019.2 | 
| he: Hebrew | Documentation from Feb 2017. NVDA interface Up to date. | 2019.2 |
| hi: Hindi | NVDA interface up to date | 2019.2 |
| hr: Croatian | Up to date. | 2019.2 |
| hu: Hungarian | Up to date. | 2018.3 |
| is: Icelandic | Not complete, intermittent, help needed. | Apr 2013 |
| it: Italian | Up to date. | 2018.3 | 
| ja: Japanese | Up to date. | 2018.3 | 
| ka: Georgian | Not complete/out of date, maintainer needed. | May 2015 |
| kmr: Northern Kurdish | In progress. | N/A |
| kn: Kannada | Out of date, help needed. | Date unknown |
| ko: Korean | Up to date. | 2018.3 |
| ky: Kyrgyz | Up to date. | 2018.3 |
| lt: Lithuanian | Out of date, help needed. | 2016 |
| lv: Latvian | Out of date, help needed. | 2016 |
| mk: Macedonian | Up to date. | 2017.4 |
| mn: Mongolian | Up to date. | 2018.2 |
| my: Burmese | Up to date. | 2018.3 |
| nb_NO: Norwegian | Out of date. | 2012 |
| ne: Nepali  | Translator deceased. | 2016 |
| nl: Dutch | Up to date. | 2018.3 |
| Pa: Punjabi | Not complete, help needed. | Nov 2014 |
| pl: Polish | Up to date. | 2018.3 |
| pt_BR: Portuguese (Brazil) | Up to date. | 2018.3 |
| pt_PT: Portuguese (Portugal) | Up to date. | 2018.3 |
| ro: Romanian | Up to date. | 2018.3 |
| ru: Russian | Up to date. | 2018.3 |
| sk: Slovak | Up to date. | 2018.2 |
| sl: Slovenian | Up to date. | 2018.3 |
| sq: Albanian | Not complete/out of date, maintainer needed. | Jul 2011 |
| sr: Serbian | Interface Up to date, documentation not complete. | 2018.3 |
| sv: Swedish | Not complete/out of date. | May 2015 |
| ta: Tamil | Up to date. | 2018.3 |
| th: Tai | Out of date. | Feb 2011 |
| tr: Turkish | Up to date. | 2018.3 |
| uk: Ukranian | Up to date. | 2018.3 |
| ur: Urdu | Incomplete, barely translated. | 2016 |
| vi: Vietnamese | Up to date. | 2018.3 |
| zh_CN: Simplified Chinese | Up to date. | 2018.3 |
| zh_HK: Traditional Chinese Hong Kong | Up to date. | 2018.3 |
| zh_TW: Traditional Chinese Taiwan | Up to date. | 2018.3 |

## New Localization
Start by subscribing to the translation list above, so that you can get help and advice.

It is recommended that you use our new more automated workflow, which will allow you to focus only on translation. See [the automated workflow section](#advantages-of-the-automatic-workflow-process ) below.

If you still wish to go through the manual process, then follow the instructions on the [[TranslatingUsingManualProcess]] page after first reading [Files to be Localized](#files-to-be-localized) below.

## Improving an Existing Localization
You should contact the existing maintainer of your language, and discuss your suggestions and changes. Together you should be able to agree on the best translation and terms to be used, and the necessary changes can be made.

You can send an email to the translation mailing list to find out the correct person. 

If your language is no longer maintained, you can request to be the new maintainer for the language.

## Files to be Localized
These files are listed in order of importance.

- nvda.po: NVDA's interface messages, see [[TranslatingTheInterface]] page for more info.
- characterDescriptions.dic: names of characters in your language, see [[TranslatingCharacterDescriptions]] for more info.
- symbols.dic: names of symbols and punctuation in your language, see [[TranslatingSymbols]] for more information.
- userGuide.t2t: the User Guide, see [[TranslatingUserGuide]] for more information.
- changes.t2t (optional): a list of changes between releases, see [[TranslatingChanges]] for more information.
- Add-ons (optional): a set of optional features that users can install, see [[TranslatingAddons]] for more information.

## Advantages of the Automatic Workflow Process
- No need of a full NVDA development environment.
- You will be sent an email or twitter message when your po file needs updating.
- You will be sent an email or twitter message when your userGuide or changes file needs to be updated.
- Automatic generation of html from t2t files, so that you can check the correctness of your t2t markup.
- Automatically generated difference and word difference between previous and new versions, to help you quickly find the changes.
- A higher quality User Guide since the difference files encourage you to keep the English and your localization closely updated.
- Translation becomes many small tasks instead a big rush near a deadline. Maybe 10 minutes per week on average.
- It is easier to contribute, since each work unit is self contained.
- Your translation is regularly and automatically included into NVDA snapshots.
- Instead of following nvda-dev mailing list emails, you can just subscribe to nvda translations and important messages related to translation will be sent there.
- Auto generated structure difference between the English and your localized user guide, to quickly spot missing paragraphs, tables and lists.
- Automatic checking of po files, making sure that there are no mistakes that could cause any runtime errors.

If you want to follow the automatic workflow process, visit the [[TranslatingUsingAutomaticProcess]] page.

## Missing information
Please feel free to update this or any subsequent page with any tips or hints that you feel may be of use to other translators.

### Missing Sections
If someone could add Sites for Gestures.ini, it'll be done.