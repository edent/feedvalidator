"""$Id$"""

__author__ = "Sam Ruby <http://intertwingly.net/> and Mark Pilgrim <http://diveintomark.org/>"
__version__ = "$Revision$"
__date__ = "$Date$"
__copyright__ = "Copyright (c) 2002 Sam Ruby and Mark Pilgrim"
__license__ = "Python"

from base import validatorBase

#
# Main document.  
# Supports rss, rdf, pie, and ffkar
#
class root(validatorBase):
  purl1_namespace='http://purl.org/rss/1.0/'
  purl2_namespace='http://purl.org/rss/2.0/'
  soap_namespace='http://feeds.archive.org/validator/'
  pie_namespace='http://purl.org/atom/ns#'

  def __init__(self, parent):
    validatorBase.__init__(self)
    self.parent = parent
    self.dispatcher = parent
    self.name = "root"

  def startElementNS(self, name, qname, attrs):
    if name=='rss':
      validatorBase.defaultNamespaces.append(qname)
    if name=='channel':
      validatorBase.defaultNamespaces.append(self.purl2_namespace)
    if name=='feed':
      if not qname:
        from logging import MissingNamespace
        self.log(MissingNamespace({"parent":"root", "element":name}))
      validatorBase.defaultNamespaces.append(self.pie_namespace)

    validatorBase.startElementNS(self, name, qname, attrs)

  def unknown_starttag(self, name, qname, attrs):
    from logging import ObsoleteNamespace,InvalidNamespace,UndefinedElement
    if qname in ['http://example.com/newformat#']:
      self.log(ObsoleteNamespace({"element":name, "namespace":qname}))
    elif name=='feed':
      self.log(InvalidNamespace({"element":name, "namespace":qname}))
    else:
      self.log(UndefinedElement({"parent":"root", "element":name}))

    from validators import eater
    return eater()

  def do_rss(self):
    from rss import rss
    return rss()

  def do_feed(self):
    from feed import feed
    return feed()

  def do_rdf_RDF(self):
    from rdf import rdf
    validatorBase.defaultNamespaces.append(self.purl1_namespace)
    return rdf()

  def do_channel(self):
    from channel import channel
    return channel()

  def do_soap_Envelope(self):
    return root(self)

  def do_soap_Body(self):
    validatorBase.defaultNamespaces.append(self.soap_namespace)
    return root(self)

  def do_request(self):
    return root(self)

  def do_xhtml_html(self):
    from logging import UndefinedElement
    self.log(UndefinedElement({"parent":"root", "element":"xhtml:html"}))
    from validators import eater
    return eater()

__history__ = """
$Log$
Revision 1.1  2004/02/03 17:33:16  rubys
Initial revision

Revision 1.18  2003/12/11 16:32:08  f8dy
fixed id tags in header

Revision 1.17  2003/08/23 21:01:00  rubys
Validate that content, content:encoded, and xhtml:body are safe

Revision 1.16  2003/08/05 07:59:04  rubys
Add feed(id,tagline,contributor)
Drop feed(subtitle), entry(subtitle)
Check for obsolete version, namespace
Check for incorrect namespace on feed element

Revision 1.15  2003/08/05 05:32:35  f8dy
0.2 snapshot - change version number and default namespace

Revision 1.14  2003/08/04 00:54:35  rubys
Log every valid element (for better self validation in test cases)

Revision 1.13  2003/07/09 16:24:30  f8dy
added global feed type support

Revision 1.12  2003/07/07 10:35:50  rubys
Complete first pass of echo/pie tests

Revision 1.11  2003/07/07 00:54:00  rubys
Rough in some pie/echo support

Revision 1.10  2002/12/22 23:56:09  rubys
Adjust names, add a WSDL

Revision 1.9  2002/10/18 13:06:57  f8dy
added licensing information

"""