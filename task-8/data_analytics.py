import json


class JsonBaseData:

    def __init__(self, data):
        self.data = data

    def get_json(self):
        return self.data


class JsonAnalytics:

    def __init__(self):
        pass

    def get_analytics(self, json_base_data: JsonBaseData):
        # do some analytics with this data
        return json_base_data.get_json()


class XmlBaseData:
    def __init__(self, data):
        self.data = data

    def get_xml(self):
        return self.data


class XmlJsonAdapter(JsonBaseData):
    def __init__(self, xml_base_data: XmlBaseData):
        self.xml_base_data = xml_base_data

    def get_json(self):
        return self.convert_xml_to_json(self.xml_base_data.get_xml())

    def convert_xml_to_json(self, xml_data):
        json_data = {}
        for key, value in xml_data.items():
            if isinstance(value, dict):
                json_data[key] = self.convert_xml_to_json(value)
            else:
                json_data[key] = value
        return json_data


json_first_name_data = JsonBaseData(json.loads('{"name": "sameer"}'))
xml_last_name_data = XmlBaseData({'name': 'ahmed'})
xml_json_adapter = XmlJsonAdapter(xml_last_name_data)
json_analytics = JsonAnalytics()
print(json_analytics.get_analytics(json_first_name_data))
print(json_analytics.get_analytics(xml_json_adapter))
