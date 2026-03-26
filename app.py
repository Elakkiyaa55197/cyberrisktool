from flask import Flask, request, jsonify
import nmap

app = Flask(__name__)

def scan_target(target):
    nm = nmap.PortScanner()
    nm.scan(target, '1-1024')
    return nm[target]['tcp']

def calculate_risk(open_ports):
    score = len(open_ports) * 10
    if score > 80:
        return "High Risk"
    elif score > 40:
        return "Medium Risk"
    else:
        return "Low Risk"

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    ip = data['ip']
    
    try:
        ports = scan_target(ip)
        risk = calculate_risk(ports)
        
        return jsonify({
            "ports": list(ports.keys()),
            "risk": risk
        })
    except:
        return jsonify({"error": "Scan failed"})

app.run(debug=True)