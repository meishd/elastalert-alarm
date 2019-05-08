# -*- coding: utf-8 -*-

from staticconf.loader import yaml_loader

config_path='/root/elastalert-0.1.38/myalert/elastalert-alarm'

def load_contact(filename):
    loaded = yaml_loader(filename)
    return loaded


def get_all_contact(members,contact_type):
    contacts = set()
    for mem_contacts in members.values():
        contacts.add(str(mem_contacts.get(contact_type,None)))
    return contacts

def get_contact_conf():
    filename = config_path + '/config-contact.yaml'
    return load_contact(filename)

def get_contact_by_domain(domain,contact_type):
    contacts = set()
    contact_conf = get_contact_conf()
    project = domain.split('_')[0]
    project_str2int = int(project) if project.isdigit() else project
    contacts_yw = get_all_contact(contact_conf['yunwei']['member'],contact_type)
    contacts = contacts_yw
    if contact_conf.get(project_str2int):
        contacts_proj = get_all_contact(contact_conf[project_str2int]['member'], contact_type)
        contacts = contacts | contacts_proj
    return contacts


def get_dingtoken_by_domain(domain):
    tokens = set()
    contact_conf = get_contact_conf()
    project = domain.split('_')[0]
    project_str2int = int(project) if project.isdigit() else project

    if contact_conf['yunwei'].get('dingtoken'):
        token_yw = contact_conf['yunwei']['dingtoken']
        if token_yw:
            tokens.add(token_yw)

    if contact_conf.get(project_str2int):
        token_proj = contact_conf[project_str2int].get('dingtoken')
        if token_proj:
            tokens.add(token_proj)

    return tokens


