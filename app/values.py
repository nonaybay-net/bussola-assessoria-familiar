pictures = {
    'ibiuna': [
        'https://ik.imagekit.io/czdfjw711v/755f56a0/62226cd6/tr:w-620/0001_W0OYNppUW.webp',
        'https://ik.imagekit.io/czdfjw711v/755f56a0/62226cd6/tr:w-620/0002_KRiCkO6UP.webp',
        'https://ik.imagekit.io/czdfjw711v/755f56a0/62226cd6/tr:w-620/0003_6zA-AdIe2.webp',
        'https://ik.imagekit.io/czdfjw711v/755f56a0/62226cd6/tr:w-620/0004_6iM0TNYsg.webp',
    ],
}

pictures_names = {
    'ibiuna': 'Ibiúna',
}

favicon_srcs = ['apple-touch-icon', 'icon',]
favicon_sizes = [
    '16', '32', '57', '60', '72', '76', '96', '114', '120', '144', '152', '180', '192',
]


owner_name = 'Marcelo Paulino da Silva'
owner_doc = 'CRTH-BR 12699'
owner_email = 'bafmps@proton.me'
owner_phone = '11932983760'
dev_name = 'Rafael Venancio'
dev_doc = None
dev_email = 'rafaelvenancio@protonmail.com'
dev_phone = None
proj_name = 'Bússola Assessoria Familiar'
proj_desc = '{} especializada em dependência química e alcoólica'.format(proj_name)
proj_lang = 'pt'
proj_local = 'BR'
proj_langfull = '{}_{}'.format(proj_lang, proj_local)
proj_owner = owner_name
proj_author = proj_owner
proj_favicon = 'https://ik.imagekit.io/czdfjw711v/755f56a0/tr:w-24/favicon_uF2AvVbE0.webp'



context = {
    # about owner
    'o_name'            :   owner_name,
    'o_doc'             :   owner_doc,
    'o_email'           :   owner_email,
    'o_phone'           :   owner_phone,
    # about developer
    'd_name'            :   dev_name,
    'd_doc'             :   dev_doc,
    'd_email'           :   dev_email,
    'd_phone'           :   dev_phone,
    # about project
    'name'              :   proj_name,
    'desc'              :   proj_desc,
    'lang'              :   proj_lang,
    'local'             :   proj_local,
    'lcode'             :   proj_langfull,
    'owner'             :   proj_owner,
    'author'            :   proj_author,
    'icon'              :   proj_favicon,
    'icon_srcs'         :   favicon_srcs,
    'icon_sizes'        :   favicon_sizes,

    # pictures
    'pics': pictures,
    'pics_l_names': pictures_names,
}
