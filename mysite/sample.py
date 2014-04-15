

AUTH_LDAP_SERVER_URI = "ldap://10.0.3.15"

import ldap

AUTH_LDAP_CONNECTION_OPTIONS = {
	ldap.OPT_REFERRALS: 0
}

AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=admin,dc=test,dc=com"

import logging

logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
