import os
import openai
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

openai.api_key = os.getenv("OPENAI_API")

data = pd.read_csv('data_with_title.csv')
data['summary'] = None

prompt = '''
For the above text, give me an assessment in JSON format of:
1. What are the threat procedures (“What is happening?”)
2. What are the threat tactics (“Why is this happening?”)
3. What are the threat techniques (“How is this happening?”)

Ensure that where possible, you include the metadata listed in the below example.

{
  "ID": "Advisory ID",
  "URL": "URL to the advisory",
  "Title": "Title of the Advisory",
  "Release Date": "Date of release",
  "Last Updated": "Date of last update",
  "Severity": "Severity level",
  "Affected Systems": [
	"List of affected systems or sectors"
  ],
  "Summary": "Brief summary of the advisory",
  "Procedures": {
	"Key Procedure 1": "Description of the procedure",
	"Key Procedure 2": "Description of the procedure"
  },
  "Tactics": {
	"Tactic 1": "Description of the tactic",
	"Tactic 2": "Description of the tactic",
	"Tactic 3": "Description of the tactic"
  },
  "Techniques": {
	"Technique 1": "Description of the technique",
	"Technique 2": "Description of the technique",
	"Technique 3": "Description of the technique"
  },
  "Threat Actions": [
	"List of specific actions taken by the threat actors"
  ],
  "Indicators of Compromise": {
	"IPs": [
  	"List of suspicious IP addresses"
	],
	"Domains": [
  	"List of suspicious domain names"
	],
	"Hashes": [
  	"List of file or malware hashes"
	]
  },
  "Mitigation Strategies": "Recommended actions to mitigate the threat",
  "References": [
	"Links to additional resources or related advisories"
  ]
}



EXAMPLES

—-----
{
  "ID": "AA24-109A",
  "URL": "https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a",
  "Title": "#StopRansomware: Akira Ransomware",
  "Release Date": "2024-04-18",
  "Last Updated": "2024-04-18",
  "Severity": "High",
  "Affected Systems": [
	"Windows Systems",
	"VMware ESXi Virtual Machines"
  ],
  "Summary": "This advisory outlines the activities of Akira ransomware, which targets critical infrastructures globally, impacting over 250 entities and generating around $42 million in ransom payments.",
  "Procedures": {
	"Exploitation": "Akira ransomware actors exploit system vulnerabilities and insecure configurations to deploy ransomware, targeting critical infrastructure for financial gain.",
	"Adaptation": "Actors adapt their approaches and tools to overcome defensive measures, employing sophisticated ransomware variants like Megazord and Akira_v2."
  },
  "Tactics": {
	"InitialAccess": "Threat actors use various methods such as exploiting VPN vulnerabilities, RDP, and phishing to gain initial access to target systems.",
	"Persistence": "Actors maintain access through techniques like creating new domain accounts and using administrative tools for network surveillance.",
	"DefenseEvasion": "They employ methods to disable antivirus and other security measures to avoid detection."
  },
  "Techniques": {
	"CredentialAccess": "Use of credential harvesting tools like Mimikatz and techniques like Kerberoasting to escalate privileges within networks.",
	"LateralMovement": "Employment of various tools to move laterally within networks and maintain control over critical systems.",
	"DataExfiltration": "Use of FileZilla, WinSCP, and other tools to exfiltrate data securely, often leveraging multiple protocols like FTP and SFTP.",
	"Impact": "Implementation of a double-extortion model by encrypting critical data and threatening to release it unless ransoms are paid."
  },
  "Threat Actions": [
	"Deployment of Akira and Megazord ransomware variants",
	"Encryption of sensitive data",
	"Exfiltration of critical information"
  ],
  "Indicators of Compromise": {
	"IPs": [
  	"192.168.1.1",
  	"10.0.0.2"
	],
	"Domains": [
  	"malicious.com",
  	"example.net"
	],
	"Hashes": [
  	"abc123",
  	"def456"
	]
  },
  "Mitigation Strategies": "Organizations are advised to update all systems to the latest security patches, implement multifactor authentication, and conduct regular security audits to limit exposure to ransomware attacks.",
  "References": [
	"https://stopransomware.gov",
	"https://www.cisa.gov/tlp"
  ]
}



{
  "ID": "AA24-038A",
  "URL": "https://www.cisa.gov/tlp",
  "Title": "PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure",
  "Release Date": "2024-02-07",
  "Last Updated": "2024-02-07",
  "Severity": "Critical",
  "Affected Systems": [
	"Communications, Energy, Transportation Systems, and Water and Wastewater Systems"
  ],
  "Summary": "This advisory by CISA, NSA, and FBI assesses that PRC state-sponsored cyber actors are positioning themselves within IT networks of critical U.S. infrastructure to enable potential disruptive cyberattacks.",
  "Procedures": {
	"Pre-positioning": "PRC state-sponsored actors compromise IT environments of critical infrastructure to facilitate later disruptive actions, possibly in response to geopolitical tensions.",
	"Persistent Access": "These actors maintain long-term, stealthy presence within compromised networks to continuously gather intelligence and prepare for potential disruptions."
  },
  "Tactics": {
	"Initial Access": "Actors exploit public-facing applications and valid accounts to gain initial footholds.",
	"Persistence": "Using valid credentials and various evasion techniques, actors maintain persistent access to victim networks.",
	"Lateral Movement": "Actors move laterally within the network to reach critical operational technology (OT) assets, aiming to position themselves for disruptive activities."
  },
  "Techniques": {
	"Credential Access": "Actors use techniques like credential dumping, privilege escalation, and exploiting software vulnerabilities to gain elevated network access.",
	"Discovery": "They perform extensive network reconnaissance to map out network architecture, identify critical assets, and understand security measures.",
	"Defense Evasion": "The use of living-off-the-land techniques and the manipulation of legitimate system processes help the actors avoid detection."
  },
  "Threat Actions": [
	"Compromise of multiple critical infrastructure networks across sectors such as energy and water systems",
	"Use of advanced persistent threats for strategic cyber espionage and pre-positioning for potential attacks"
  ],
  "Indicators of Compromise": {
	"IPs": [
  	"Varies - specific IPs not listed in the provided text"
	],
	"Domains": [
  	"Varies - specific domains not listed in the provided text"
	],
	"Hashes": [
  	"Varies - specific hashes not listed in the provided text"
	]
  },
  "Mitigation Strategies": "The advisory recommends immediate actions like patching known vulnerabilities, implementing phishing-resistant multifactor authentication, and ensuring proper security logging and segmentation to mitigate the threat from these actors.",
  "References": [
	"https://www.cisa.gov/china-cyber-threat-overview-and-advisories",
	"https://www.cisa.gov/tlp"
  ]
}



'''

for index, row in data.iterrows():
    text = data['text'][index]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", 
                "content": text + "\n\n\n\n\n" + prompt}
            ]
        )
        data.at[index, 'summary'] = response.choices[0].message.content  
        print(response.choices[0].message.content)
    except Exception as e:
        print("An error occurred:", e)

data.to_csv('data_with_summary.csv', index=False)