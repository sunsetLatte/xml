def read_xml(file, len_word=6, top_words=10):
   tree = ET.parse(file)
   root = tree.getroot()
   xml_items = root.findall('channel/item')
   description_words = []
   descriptions = [item.find('description').text.split() for item in xml_items]
   for description in descriptions:
       description = [word for word in description if len(word) > len_word]
       description_words.extend(description)
   counter_words = collections.Counter(description_words)
   pprint(counter_words.most_common(top_words))


if __name__ == '__main__':
   read_json('newsafr.json')
   print('------')
   read_xml('newsafr.xml')