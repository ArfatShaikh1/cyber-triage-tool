class IOCDetector:
    def __init__(self):
        # Initialize IOC patterns
        self.ioc_patterns = {
            'malicious_ips': [],
            'suspicious_domains': [],
            'malicious_hashes': []
        }

    def add_malicious_ip(self, ip):
        if ip not in self.ioc_patterns['malicious_ips']:
            self.ioc_patterns['malicious_ips'].append(ip)

    def add_suspicious_domain(self, domain):
        if domain not in self.ioc_patterns['suspicious_domains']:
            self.ioc_patterns['suspicious_domains'].append(domain)

    def add_malicious_hash(self, file_hash):
        if file_hash not in self.ioc_patterns['malicious_hashes']:
            self.ioc_patterns['malicious_hashes'].append(file_hash)

    def detect_malicious_ip(self, ip):
        return ip in self.ioc_patterns['malicious_ips']

    def detect_suspicious_domain(self, domain):
        return domain in self.ioc_patterns['suspicious_domains']

    def detect_malicious_hash(self, file_hash):
        return file_hash in self.ioc_patterns['malicious_hashes']

# Example usage:
# ioc_detector = IOCDetector()
# ioc_detector.add_malicious_ip('192.168.1.1')
# print(ioc_detector.detect_malicious_ip('192.168.1.1'))  # True
