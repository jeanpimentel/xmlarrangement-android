#!/usr/bin/env python
# coding: utf-8

from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, tostring

import sys

NS = {
    'android': 'http://schemas.android.com/apk/res/android',
    'app': 'http://schemas.android.com/apk/res-auto',
    'tools': 'http://schemas.android.com/tools',
}


def generate(filename):
    xml = ''
    with open(filename, mode='r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            xml += generate_rule_for(line)
    print xml


def generate_rule_for(line):
    if 'xmlns' in line:
        return generate_xml_for(line, '^$', '.*' in line)

    if line == 'style':
        return generate_xml_for(line, '^$', '.*' in line)

    if ':' in line:
        namespace, attrib = line.split(':')
    else:
        namespace, attrib = None, line

    if namespace in NS:
        namespace = NS[namespace]
    else:
        namespace = '^$'

    with_order = '.*' in attrib

    if attrib != '.*':
        attrib = '.*:' + attrib

    return generate_xml_for(attrib, namespace, with_order)


def generate_xml_for(name, ns, with_order=False):
    """
    <section>
      <rule>
        <match>
          <AND>
            <NAME>xmlns:android</NAME>
            <XML_NAMESPACE>^$</XML_NAMESPACE>
          </AND>
        </match>
        <order>BY_NAME</order>
      </rule>
    </section>
    """
    section = Element('section')
    rule = SubElement(section, 'rule')
    match = SubElement(rule, 'match')
    AND = SubElement(match, 'AND')

    NAME = SubElement(AND, 'NAME')
    NAME.text = name

    XML_NAMESPACE = SubElement(AND, 'XML_NAMESPACE')
    XML_NAMESPACE.text = ns

    if with_order:
        order = SubElement(rule, 'order')
        order.text = 'BY_NAME'

    return toprettyxml(section)


def toprettyxml(section):
    reparsed = minidom.parseString(tostring(section, 'utf-8'))
    return reparsed.toprettyxml(indent='  ') \
        .replace(u'<?xml version="1.0" ?>\n', '')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        generate(sys.argv[1])
    else:
        sys.exit('Usage: %s FILE' % sys.argv[0])
