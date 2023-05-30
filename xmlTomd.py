import xml.etree.ElementTree as ET
from tabulate import tabulate
import argparse

def parse_nmap_xml(xmlfile):
    # Parse XML
    tree = ET.parse(xmlfile)
    root = tree.getroot()

    for host in root.findall('host'):
        # Get IP address
        ip = host.find('address').get('addr')
        print(f"## {ip}\n")

        # Prepare data for table
        table_data = []
        for port in host.iter('port'):
            # Get port details
            port_id = f"{port.get('portid')}/{port.get('protocol')}"
            service = port.find('service').get('name')
            product = port.find('service').get('product')
            version = port.find('service').get('version')
            extrainfo = port.find('service').get('extrainfo')

            # Combine all service details and filter out None values
            service_info_parts = [service, product, version, extrainfo]
            service_info = " ".join(part for part in service_info_parts if part)

            table_data.append([port_id, service_info])
        
        # Create and print table
        table = tabulate(table_data, headers=['Port', 'Service'], tablefmt="pipe")
        print(table)
        print("\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse an Nmap XML file.')
    parser.add_argument('xmlfile', type=str, help='Path to the XML file')
    args = parser.parse_args()
    
    parse_nmap_xml(args.xmlfile)

