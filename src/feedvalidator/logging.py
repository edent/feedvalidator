"""$Id$"""

__author__ = "Sam Ruby <http://intertwingly.net/> and Mark Pilgrim <http://diveintomark.org/>"
__version__ = "$Revision$"
__date__ = "$Date$"
__copyright__ = "Copyright (c) 2002 Sam Ruby and Mark Pilgrim"
__license__ = "Python"

# feed types
TYPE_UNKNOWN = 0
TYPE_RSS1 = 1
TYPE_RSS2 = 2
TYPE_ATOM = 3

FEEDTYPEDISPLAY = {0:"(unknown type)", 1:"RSS", 2:"RSS", 3:"Atom"}

VALIDFEEDGRAPHIC = {0:"", 1:"valid-rss.png", 2:"valid-rss.png", 3:"valid-atom.png"}

#
# logging support
#

class LoggedEvent:
  def __init__(self, params):
    self.params = params
class Info(LoggedEvent): pass
class Warning(LoggedEvent): pass
class Error(LoggedEvent): pass

###################### error ######################

class SAXError(Error): pass
class UnicodeError(Error): pass

class UndefinedElement(Error): pass
class MissingNamespace(UndefinedElement): pass
class NoBlink(UndefinedElement): pass
class MissingAttribute(Error): pass
class DuplicateElement(Error): pass
class NotEnoughHoursInTheDay(Error): pass
class EightDaysAWeek(Error): pass

class InvalidValue(Error): pass
class InvalidContact(InvalidValue): pass
class InvalidLink(InvalidValue): pass
class InvalidW3DTFDate(InvalidValue): pass
class InvalidRFC2822Date(InvalidValue): pass
class InvalidURLAttribute(InvalidValue): pass
class InvalidIntegerAttribute(InvalidValue): pass
class InvalidBooleanAttribute(InvalidValue): pass
class InvalidMIMEAttribute(InvalidValue): pass
class NotBlank(InvalidValue): pass
class AttrNotBlank(InvalidValue): pass
class InvalidInteger(InvalidValue): pass
class InvalidWidth(InvalidValue): pass
class InvalidHeight(InvalidValue): pass
class InvalidHour(InvalidValue): pass
class InvalidDay(InvalidValue): pass
class InvalidHttpGUID(InvalidValue): pass
class InvalidLanguage(InvalidValue): pass
class InvalidUpdatePeriod(InvalidValue): pass
class ContainsUndeclaredHTML(InvalidValue): pass

class MissingElement(Error): pass
class MissingChannel(MissingElement): pass
class MissingDescription(MissingElement): pass
class MissingLink(MissingElement): pass
class MissingTitle(MissingElement): pass
class ItemMustContainTitleOrDescription(MissingElement): pass

class FatalSecurityRisk(Error): pass
class ContainsSystemEntity(FatalSecurityRisk): pass

class DuplicateValue(InvalidValue): pass

class InvalidDoctype(Error): pass

class MultipartInvalid(Error): pass
class MultipartMissing(Error): pass
class MultipartRecursion(Error): pass
class MultipartDuplicate(Error): pass

class DuplicateAtomLink(Error): pass
class MissingHref(Error): pass
class AtomLinkNotEmpty(Error): pass
class AtomLinkMissingRel(Error): pass
class MissingAlternateLink(Error): pass

###################### warning ######################

class DuplicateSemantics(Warning): pass
class DuplicateItemSemantics(DuplicateSemantics): pass

class ContainsRelRef(Warning): pass

class ReservedPrefix(Warning): pass

class SecurityRisk(Warning): pass
class ContainsScript(SecurityRisk): pass
class ContainsMeta(SecurityRisk): pass
class ContainsEmbed(SecurityRisk): pass
class ContainsObject(SecurityRisk): pass

###################### info ######################

class ContainsHTML(Info): pass

class MissingOptionalElement(Info): pass
class MissingItemLink(MissingOptionalElement): pass
class MissingItemTitle(MissingOptionalElement): pass

class BestPractices(Info): pass

class MissingRecommendedElement(BestPractices): pass
class MissingDCLanguage(MissingRecommendedElement): pass
class MissingDCRights(MissingRecommendedElement): pass
class MissingDCDate(MissingRecommendedElement): pass

class UseModularEquivalent(BestPractices): pass
class UseDCRights(UseModularEquivalent): pass
class UseAdminGeneratorAgent(UseModularEquivalent): pass
class UseDCCreator(UseModularEquivalent): pass
class UseDCSubject(UseModularEquivalent): pass
class UseDCDate(UseModularEquivalent): pass
class UseDCSource(UseModularEquivalent): pass
class UseDCLanguage(UseModularEquivalent): pass
class UseDCTermsModified(UseModularEquivalent): pass
class UseDCPublisher(UseModularEquivalent): pass
class UseSyndicationModule(UseModularEquivalent): pass
class UseAnnotateReference(UseModularEquivalent): pass

class RecommendedWidth(BestPractices): pass
class RecommendedHeight(BestPractices): pass

class NonstdPrefix(BestPractices): pass

## Atom-specific errors
class ObsoleteVersion(Error): pass
class ObsoleteNamespace(Error): pass

class InvalidURI(InvalidValue) : pass
class InvalidURN(InvalidValue): pass
class InvalidTAG(InvalidValue): pass
class InvalidContentMode(InvalidValue) : pass
class InvalidMIMEType(InvalidValue) : pass
class InvalidNamespace(Error): pass
class NoMIMEType(MissingAttribute) : pass
class NotEscaped(InvalidValue): pass
class NotBase64(InvalidValue): pass
class NotInline(Warning): pass # this one can never be sure...
class NotHtml(Error): pass

class W3DTFDateNoTimezone(Warning) : pass
class W3DTFDateNonUTC(Info) : pass
class W3DTFDateNonLocal(Warning) : pass

############## non-errors (logging successes) ###################

class Success(LoggedEvent): pass

class ValidValue(Success): pass
class ValidCloud(Success): pass

class ValidURI(ValidValue): pass
class ValidHttpGUID(ValidURI): pass
class ValidURLAttribute(ValidURI): pass
class ValidURN(ValidValue): pass
class ValidTAG(ValidValue): pass
class ValidTitle(ValidValue): pass

class ValidDate(ValidValue): pass
class ValidW3DTFDate(ValidDate): pass
class ValidRFC2822Date(ValidDate): pass

class ValidAttributeValue(ValidValue): pass
class ValidBooleanAttribute(ValidAttributeValue): pass

class ValidLanguage(ValidValue): pass
class ValidHeight(ValidValue): pass
class ValidWidth(ValidValue): pass
class ValidTitle(ValidValue): pass
class ValidContact(ValidValue): pass
class ValidIntegerAttribute(ValidValue): pass
class ValidMIMEAttribute(ValidValue): pass
class ValidDay(ValidValue): pass
class ValidHour(ValidValue): pass
class ValidInteger(ValidValue): pass
class ValidUpdatePeriod(ValidValue): pass
class ValidContentMode(ValidValue): pass
class ValidElement(ValidValue): pass
class ValidCopyright(ValidValue): pass
class ValidGeneratorName(ValidValue): pass
class OptionalValueMissing(ValidValue): pass
class ValidDoctype(ValidValue): pass
class ValidHtml(ValidValue): pass
class ValidAtomLinkRel(ValidValue): pass

__history__ = """
$Log$
Revision 1.1  2004/02/03 17:33:16  rubys
Initial revision

Revision 1.63  2003/12/12 15:00:22  f8dy
changed blank link attribute tests to new error AttrNotBlank to distinguish them from elements that can not be blank

Revision 1.62  2003/12/12 14:23:19  f8dy
ValidAtomLinkRel should inherit from ValidValue

Revision 1.61  2003/12/12 05:42:05  rubys
Rough in some support for the new link syntax

Revision 1.60  2003/12/12 01:24:36  rubys
Multipart/alternative tests

Revision 1.59  2003/12/11 18:20:46  f8dy
passed all content-related testcases

Revision 1.58  2003/12/11 16:32:08  f8dy
fixed id tags in header

Revision 1.57  2003/12/11 06:00:51  f8dy
added tag: testcases, passed

Revision 1.56  2003/08/24 00:05:34  f8dy
removed iframe tests, after further discussion this is not enough of a security risk to keep feeds from validating

Revision 1.55  2003/08/23 01:45:22  f8dy
added ContainsIframe

Revision 1.54  2003/08/23 00:28:04  rubys
Validate escaped text/HTML content

Revision 1.53  2003/08/06 16:16:59  f8dy
added testcase for Netscape DOCTYPE

Revision 1.52  2003/08/06 16:10:04  f8dy
added testcase for Netscape DOCTYPE

Revision 1.51  2003/08/05 18:01:37  f8dy
*** empty log message ***

Revision 1.50  2003/08/05 07:59:04  rubys
Add feed(id,tagline,contributor)
Drop feed(subtitle), entry(subtitle)
Check for obsolete version, namespace
Check for incorrect namespace on feed element

Revision 1.49  2003/08/05 05:37:42  f8dy
0.2 snapshot - add test for obsolete 0.1 version

Revision 1.48  2003/08/04 01:05:33  rubys
Check for HTML in titles

Revision 1.47  2003/08/04 00:54:35  rubys
Log every valid element (for better self validation in test cases)

Revision 1.46  2003/08/03 18:46:04  rubys
support author(url,email) and feed(author,copyright,generator)

Revision 1.45  2003/07/29 21:48:10  f8dy
tightened up test cases, added parent element check, changed negative test cases to positive

Revision 1.44  2003/07/29 20:57:39  f8dy
tightened up test cases, check for parent element, explicitly test for success

Revision 1.43  2003/07/29 19:38:07  f8dy
changed test cases to explicitly test for success (rather than the absence of failure)

Revision 1.42  2003/07/29 17:13:17  f8dy
more urn tests

Revision 1.41  2003/07/29 16:44:56  f8dy
changed test cases to explicitly test for success (rather than the absence of failure)

Revision 1.40  2003/07/29 15:46:31  f8dy
changed test cases to explicitly test for success (rather than the absence of failure)

Revision 1.39  2003/07/29 15:15:33  f8dy
added tests for invalid URNs (may be used in entry/id of Atom feeds)

Revision 1.38  2003/07/20 17:44:27  rubys
Detect duplicate ids and guids

Revision 1.37  2003/07/19 21:15:08  f8dy
added tests and logging classes for duplicate guid/id values within a feed (thanks AaronSw for this idea)

Revision 1.36  2003/07/11 17:47:04  rubys
not-inline can only be a warning as one can never be totally sure...

Revision 1.35  2003/07/09 19:28:39  f8dy
added test cases looking at actual content vs. mode (note: not passed)

Revision 1.34  2003/07/09 16:24:30  f8dy
added global feed type support

Revision 1.33  2003/07/09 03:31:36  f8dy
Updated pie-specific log messages

Revision 1.32  2003/07/07 10:35:50  rubys
Complete first pass of echo/pie tests

Revision 1.31  2003/07/07 00:54:00  rubys
Rough in some pie/echo support

Revision 1.30  2003/07/06 21:20:02  rubys
Refactor so test cases are organized by protocol

Revision 1.29  2002/10/30 23:03:01  f8dy
security fix: external (SYSTEM) entities

Revision 1.28  2002/10/27 18:54:30  rubys
Issue warnings for relative references in descriptions

Revision 1.27  2002/10/22 16:24:04  f8dy
added UnicodeError support for feeds that declare utf-8 but use 8-bit characters anyway

Revision 1.26  2002/10/18 19:28:43  f8dy
added testcases for mod_syndication and passed them

Revision 1.25  2002/10/18 14:17:30  f8dy
added tests for language/dc:language (must be valid ISO-639 language code
plus optional country code) and passed them

Revision 1.24  2002/10/18 13:06:57  f8dy
added licensing information

"""