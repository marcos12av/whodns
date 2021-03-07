import subprocess, re, sys

datos = {
    '209.50.52.248':'server0.nomadat.cloud',
    '152.44.44.200':'server1.nomadat.cloud',
    '152.44.33.64':'server2.nomadat.cloud',
    '152.44.44.40':'mail.heu.mx',
    '152.44.44.229':'mail.ugc.mx',
    '209.50.53.177':'mail.monteverde.com.mx',
    '209.50.54.61':'mail.abcappraisers.com.mx',
    '209.50.60.116':'mail.hostify.mx',
    '94.237.46.90':'secure.tatuus.nl',
    '209.50.56.13':'mail.moetti.com',
    '209.50.60.246':'mail.rzconsultoria.com',
    '209.50.60.220':'mail.telenetdemexico.com',
    '209.50.60.126':'mail.efece.net',
    '209.50.60.54':'mail.orangecorp.mx',
    '152.44.44.24':'mail.iqfglobal.com',
    '209.50.60.170':'mail.genstudio.mx',
    '94.237.44.189':'nube.manopco.mx',
    '152.44.44.149':'secure.alteacorp.com',
    '209.50.60.43':'mail.sercam.mx',
    '209.50.62.67':'mail.aslcorporativo.com',
    '152.44.46.155':'mail.cervezaminerva.mx',
    '94.237.125.121':'mail.agroshields.com',
    '209.50.62.98':'mail.moreconsultores.com.mx',
    '209.151.153.149':'mail.aw-consulting.com.mx',
    '94.237.108.21':'mail.qlgroup.cloud',
    '209.151.152.15':'mail.consorcioregency.com'
}

def ping(subdomain, domain):
    dominio = subdomain + domain
    ping = ['ping', '-c', '1', dominio]
    runping = subprocess.run(ping, capture_output=True, text=True)
    if runping.stdout:
        ipregex = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", runping.stdout)
        return ipregex.group(0)
    else:
        return None

def server():
    subdomain = ["","webmail.", "ipv4."]
    for i in subdomain:
        temp = ping(i ,sys.argv[1])
        servername = datos.get(temp)
        if servername is None:
            servername = f'Servidor no encontrado {i} .'
        else:
            return f'{servername} en registro {i}.'
            
print (server())
