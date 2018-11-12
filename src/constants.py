from enum import Enum


class Exchange(Enum):
    RADAR_RELAY = 'RADAR_RELAY'
    PARADEX = 'PARADEX'
    DDEX = 'DDEX'
    ETHFINEX = 'ETHFINEX'
    OASIS = 'OASIS'


class OrderType(Enum):
    ASK = 'ASK'
    BID = 'BID'


tokens = {
    '0x062fdce6dd1e6addcd801a4423f981879aedcf89': 'sETH_11_15',
    '0x5493d008938d141156f65db90e907d3dfc61c36c': 'sETH_11_30',
    '0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359': 'DAI',
    '0x0d8775f648430679a709e98d2b0cb6250d2887ef': 'BAT',
    '0x0f5d2fb29fb7d3cfee444a200298f468908cc942': 'MANA',
    '0x1985365e9f78359a9b6ad760e32412f4a445e862': 'REP',
    '0x22365168c8705e95b2d08876c23a8c13e3ad72e2': 'PASS',
    '0x514910771af9ca656af840dff83e8264ecf986ca': 'LINK',
    '0x58b6a8a3302369daec383334672404ee733ab239': 'LPT',
    '0x595832f8fc6bf59c85c527fec3740a1b7a361269': 'POWR',
    '0x607f4c5bb672230e8672085532f7e901544a7375': 'RLC',
    '0x95daaab98046846bf4b2853e23cba236fa394a31': 'EMONT',
    '0x960b236a07cf122663c4303350609a66a7b288c0': 'ANT',
    '0x9d9832d1beb29cc949d75d61415fd00279f84dc2': 'DNN',
    '0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2': 'MKR',
    '0xbeb9ef514a379b997e0798fdcc901ee474b6d9a1': 'MLN',
    '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2': 'WETH',
    '0xc27a2f05fa577a83ba0fdb4c38443c0718356501': 'TAU',
    '0xd0a4b8946cb52f0661273bfbc6fd0e0c75fc6433': 'STORM',
    '0xd26114cd6ee289accf82350c8d8487fedb8a0c07': 'OMG',
    '0xd2d6158683aee4cc838067727209a0aaf4359de3': 'BNTY',
    '0xdd974d5c2e2928dea5f71b9825b8b646686bd200': 'KNC',
    '0xe0b7927c4af23765cb51314a0e0521a9645f0e2a': 'DGD',
    '0xe41d2489571d322189246dafa5ebde1f4699f498': 'ZRX',
    '0xeb2da9fac54284cea731d1f10bb34eecb3c00c14': 'POW',
    '0xf6cfe53d6febaeea051f400ff5fc14f0cbbdaca1': 'DGPT',
    '0xf970b8e36e23f7fc3fd752eea86f8be8d83375a6': 'RCN',
    '0xfa456cf55250a839088b27ee32a424d7dacb54ff': 'BTT',
    '0x01b3ec4aae1b8729529beb4965f27d008788b0eb': 'DPP',
    '0x0200412995f1bafef0d3f97c4e28ac2515ec1ece': 'FLLW',
    '0x02ec0c9e6d3c08b8fb12fec51ccba048afbc36a6': 'STBL',
    '0x0371a82e4a9d0a4312f3ee2ac9c6958512891372': 'STU',
    '0x05f4a42e251f2d52b8ed15e9fedaacfcef1fad27': 'ZIL',
    '0x076c97e1c869072ee22f8c91978c99b4bcb02591': 'CBT',
    '0x08711d3b02c8758f2fb3ab4e80228418a7f8e39c': 'EDG',
    '0x09d8b66c48424324b25754a873e290cae5dca439': 'NVT',
    '0x0abdace70d3790235af448c88547603b945604ea': 'DNT',
    '0x0cf0ee63788a0849fe5297f3407f701e122cc023': 'DATA',
    '0x0e0989b1f9b8a38983c2ba8053269ca62ec9b195': 'POE',
    '0x0f513ffb4926ff82d7f60a05069047aca295c413': 'XSC',
    '0x1063ce524265d5a3a624f4914acd573dd89ce988': 'AIX',
    '0x106aa49295b525fcf959aa75ec3f7dcbf5352f1c': 'RKT',
    '0x107c4504cd79c5d2696ea0030a8dd4e92601b82e': 'BLT',
    '0x1183f92a5624d68e85ffb9170f16bf0443b4c242': 'QVT',
    '0x12480e24eb5bec1a9d4369cab6a80cad3c0a377a': 'SUB',
    '0x12b19d3e2ccc14da04fae33e63652ce469b3f2fd': 'GRID',
    '0x168296bb09e24a88805cb9c33356536b980d3fc5': 'RHOC',
    '0x1776e1f26f98b1a5df9cd347953a26dd3cb46671': 'NMR',
    '0x177d39ac676ed1c67a2b268ad7f1e58826e5b0af': 'CDT',
    '0x1d462414fe14cf489c7a21cac78509f4bf8cd7c0': 'CAN',
    '0x1f573d6fb3f13d689ff844b4ce37794d79a7ff1c': 'BNT',
    '0x2023dcf7c438c8c8c0b0f28dbae15520b4f3ee20': 'FTR',
    '0x20f7a3ddf244dc9299975b4da1c39f8d5d75f05a': 'SPN',
    '0x23b75bc7aaf28e2d6628c3f424b3882f8f072a3c': 'VIT',
    '0x24692791bc444c5cd0b81e3cbcaba4b04acd1f3b': 'UKG',
    '0x24cebc1548e698feffb5553b8ac8043b51069faa': 'TVAL',
    '0x255aa6df07540cb5d3d297f0d0d4d84cb52bc8e6': 'RDN',
    '0x263c618480dbe35c300d8d5ecda19bbb986acaed': 'MOT',
    '0x27054b13b1b798b345b591a4d22e6562d47ea75a': 'AST',
    '0x27695e09149adc738a978e9a678f99e4c39e9eb9': 'KICK',
    '0x27dce1ec4d3f72c3e457cc50354f1f975ddef488': 'AIR',
    '0x27f610bf36eca0939093343ac28b1534a721dbb4': 'WAND',
    '0x2859021ee7f2cb10162e67f33af2d22764b31aff': 'SNTR',
    '0x340d2bde5eb28c1eed91b2f790723e3b160613b7': 'VEE',
    '0x3597bfd533a99c9aa083587b074434e61eb0a258': 'DENT',
    '0x3618516f45cd3c913f81f9987af41077932bc40d': 'PCL',
    '0x386467f1f3ddbe832448650418311a479eecfc57': 'MBRS',
    '0x3883f5e181fccaf8410fa61e12b59bad963fb645': 'THETA',
    '0x399a0e6fbeb3d74c85357439f4c8aed9678a5cbf': 'DCL',
    '0x39bb259f66e1c59d5abef88375979b4d20d98022': 'WAX',
    '0x3d1ba9be9f66b8ee101911bc36d3fb562eac2244': 'RVT',
    '0x408e41876cccdc0f92210600ef50372656052a38': 'REN',
    '0x4156d3342d5c385a87d264f90653733592000581': 'SALT',
    '0x419d0d8bdd9af5e606ae2232ed285aff190e711b': 'FUN',
    '0x41e5560054824ea6b0732e656e3ad64e20e94e45': 'CVC',
    '0x42d6622dece394b54999fbd73d108123806f6a18': 'SPANK',
    '0x44f588aeeb8c44471439d1270b3603c66a9262f1': 'SNIP',
    '0x45ed02e374aef2e4b34c04e86ad9d45891d10751': 'DFS',
    '0x4aac461c86abfa71e9d00d9a2cde8d74e4e1aeea': 'ZINC',
    '0x4ceda7906a5ed2179785cd3a40a69ee8bc99c466': 'AION',
    '0x4d8fc1453a0f359e99c9675954e656d80d996fbf': 'BEE',
    '0x4dc3643dbc642b72c158e7f3d2ff232df61cb6ce': 'AMB',
    '0x4df47b4969b2911c966506e3592c41389493953b': 'FND',
    '0x4df812f6064def1e5e029f1ca858777cc98d2d81': 'XAUR',
    '0x4f3afec4e5a3f2a6a1a411def7d7dfe50ee057bf': 'DGX',
    '0x52a7cb918c11a16958be40cba7e31e32a499a465': 'FDX',
    '0x554c20b7c486beee439277b4540a434566dc4c02': 'HST',
    '0x56ba2ee7890461f463f7be02aac3099f6d5811a8': 'CAT',
    '0x5732046a883704404f284ce41ffadd5b007fd668': 'BLZ',
    '0x5af2be193a6abca9c8817001f45744777db30756': 'ETHOS',
    '0x5b09a0371c1da44a8e24d36bf5deb1141a84d875': 'MAD',
    '0xc39e626a04c5971d770e319760d7926502975e47': 'AXPR',
    '0xc997d07b0bc607b6d1bcb6fb9d4a5579c466c3e5': 'FLIP',
    '0xd0352a019e9ab9d757776f532377aaebd36fd541': 'FSN',
    '0xd4c435f5b09f855c3317c8524cb1f586e42795fa': 'CND',
    '0xd7732e3783b0047aa251928960063f863ad022d8': 'BRM',
    '0xd8950fdeaa10304b7a7fd03a2fc66bc39f3c711a': 'WYS',
    '0xdd6c68bb32462e01705011a4e2ad1a60740f217f': 'HBT',
    '0xef2463099360a085f1f10b076ed72ef625497a06': 'SHP',
    '0xf1e48f13768bd8114a530070b43257a63f24bb12': 'E10',
    '0x5b2e4a700dfbc560061e957edec8f6eeeb74a320': 'INS',
    '0x5bc7e5f0ab8b2e10d2d0a3f21739fce62459aef3': 'ENTRP',
    '0x5ca9a71b1d01849c0a95490cc00559717fcf0d1d': 'AE',
    '0x5e3346444010135322268a4630d2ed5f8d09446c': 'LOC',
    '0x614ea929892ea43d3ea2c5e3311b01cc589bad6c': 'ENO',
    '0x6425c6be902d692ae2db752b3c268afadb099d3b': 'MWAT',
    '0x672a1ad4f667fb18a333af13667aa0af1f5b5bdd': 'CRED',
    '0x6781a0f84c7e9e846dcb84a9a5bd49333067b104': 'ZAP',
    '0x6810e776880c02933d47db1b9fc05908e5386b96': 'GNO',
    '0x6aeb95f06cda84ca345c2de0f3b7f96923a44f4c': 'BERRY',
    '0x6c6ee5e31d828de241282b9606c8e98ea48526e2': 'HOT',
    '0x744d70fdbe2ba4cf95131626614a1763df805b9e': 'SNT',
    '0x7654915a1b82d6d2d0afc37c52af556ea8983c7e': 'IFT',
    '0x7b69b78cc7fee48202c208609ae6d1f78ce42e13': 'GOAL',
    '0x7d4b8cce0591c9044a22ee543533b72e976e36c3': 'CAG',
    '0x80fb784b7ed66730e8b1dbd9820afd29931aab03': 'LEND',
    '0x814964b1bceaf24e26296d031eadf134a2ca4105': 'NEWB',
    '0x865e3707a580f9db89304005cddd050ade8873eb': 'HIRE',
    '0x88fcfbc22c6d3dbaa25af478c578978339bde77a': 'FYN',
    '0x8a854288a5976036a725879164ca3e91d30c6a1b': 'GET',
    '0x8ae4bf2c33a8e667de34b54938b0ccd03eb8cc06': 'PTOY',
    '0x8b353021189375591723e7384262f45709a3c3dc': 'TOMO',
    '0x8db54ca569d3019a2ba126d03c37c44b5ef81ef6': 'DXT',
    '0x8eb24319393716668d768dcec29356ae9cffe285': 'AGI',
    '0x8f8221afbb33998d8584a2b05749ba73c37a938a': 'REQ',
    '0x9214ec02cb71cba0ada6896b8da260736a67ab10': 'REAL',
    '0x923108a439c4e8c2315c4f6521e5ce95b44e9b4c': 'EVE',
    '0x983f6d60db79ea8ca4eb9968c6aff8cfa04b3c63': 'SNM',
    '0x9992ec3cf6a55b00978cddf2b27bc6882d88d1ec': 'POLY',
    '0x99ea4db9ee77acd40b119bd1dc4e33e1c070b80d': 'QSP',
    '0x9a005c9a89bd72a4bd27721e7a09a3c11d2b03c4': 'STAC',
    '0x9a0242b7a33dacbe40edb927834f96eb39f8fbcb': 'BAX',
    '0x9af4f26941677c706cfecf6d3379ff01bb85d5ab': 'DRT',
    '0xa017ac5fac5941f95010b12570b812c974469c2c': 'XES',
    '0xa15c7ebe1f07caf6bff097d8a589fb8ac49ae5b3': 'NPXS',
    '0xa4e8c3ec456107ea67d3075bf9e3df3a75823db0': 'LOOM',
    '0xa5fd1a791c4dfcaacc963d4f73c6ae5824149ea7': 'JNT',
    '0xa8006c4ca56f24d6836727d106349320db7fef82': 'INXT',
    '0xa87c3ec87eb802aad080df0adb331e504d327e5d': 'DALA',
    '0xac3211a5025414af2866ff09c23fc18bc97e79b1': 'DOV',
    '0xacfa209fb73bf3dd5bbfb1101b9bc999c49062a5': 'BCDT',
    '0xb24754be79281553dc1adc160ddf5cd9b74361a4': 'XRL',
    '0xb45a50545beeab73f38f31e5973768c421805e5e': 'TKR',
    '0xb4efd85c19999d84251304bda99e90b92300bd93': 'RPL',
    '0xb5a5f22694352c15b00323844ad545abb2b11028': 'ICX',
    '0xb62d18dea74045e822352ce4b3ee77319dc5ff2f': 'EVC',
    '0xb64ef51c888972c908cfacf59b47c1afbc0ab8ac': 'STORJ',
    '0xb98d4c97425d9908e66e53a6fdf673acca0be986': 'ABT',
    '0xba2184520a1cc49a6159c57e61e1844e085615b6': 'HGT',
    '0xba5f11b16b155792cf3b2e6880e8706859a8aeb6': 'ARN',
    '0xbbff862d906e348e9946bfb2132ecb157da3d4b4': 'SS',
    '0xbc86727e770de68b1060c91f6bb6945c73e10388': 'XNK',
    '0xbdc5bac39dbe132b1e030e898ae3830017d7d969': 'SNOV',
    '0xbf2179859fc6d5bee9bf9158632dc51678a4100e': 'ELF',
    '0xc12d099be31567add4e4e4d0d45691c3f58f5663': 'AUC',
    '0xc438b4c0dfbb1593be6dee03bbd1a84bb3aa6213': 'EQC',
    '0xd2fa8f92ea72abb35dbd6deca57173d22db2ba49': 'ORI',
    '0xd49ff13661451313ca1553fd6954bd1d9b6e02b9': 'ELEC',
    '0xd8912c10681d8b21fd3742244f44658dba12264e': 'PLU',
    '0xdd74a7a3769fa72561b3a69e65968f49748c690c': 'ETCH',
    '0xe25bcec5d3801ce3a794079bf94adf1b8ccd802d': 'MAN',
    '0xe81d72d14b1516e68ac3190a46c93302cc8ed60f': 'CL',
    '0xea097a2b1db00627b2fa17460ad260c016016977': 'UFR',
    '0xea11755ae41d889ceec39a63e6ff75a02bc1c00d': 'CTXC',
    '0xea1f346faf023f974eb5adaf088bbcdf02d761f4': 'TIX',
    '0xea38eaa3c86c8f9b751533ba2e562deb9acded40': 'FUEL',
    '0xeab43193cf0623073ca89db9b712796356fa7414': 'GOLDX',
    '0xeb7c20027172e5d143fb030d50f91cece2d1485d': 'EBTC',
    '0xebbdf302c940c6bfd49c6b165f457fdb324649bc': 'HYDRO',
    '0xeee2d00eb7deb8dd6924187f5aa3496b7d06e62a': 'TIG',
    '0xf433089366899d83a9f26a773d59ec7ecf30355e': 'MTL',
    '0xf6b55acbbc49f4524aa48d19281a9a77c54de10f': 'WLK',
    '0xf7b098298f7c69fc14610bf71d5e02c60792894c': 'GUP',
    '0xf860f90e1f55e3528682e18850612cbb45bbf1bc': 'DEX',
    '0xfa10e13fe555760a5297dc14eb6562a1a53e4e37': 'ETHX_5_18',
    '0xfa1a856cfa3409cfa145fa4e20eb270df3eb21ab': 'IOST',
    '0xfec0cf7fe078a500abf15f1284958f22049c2c7e': 'ART'
 }

common_tokens = ['AION',
 'AIX',
 'AUC',
 'BAT',
 'BAX',
 'BNT',
 'CAN',
 'CAT',
 'DAI',
 'DATA',
 'DGD',
 'DRT',
 'EDG',
 'ELF',
 'FTR',
 'GNO',
 'HOT',
 'KICK',
 'KNC',
 'LOC',
 'MAD',
 'MANA',
 'MKR',
 'MTL',
 'OMG',
 'POE',
 'POWR',
 'RCN',
 'REAL',
 'REQ',
 'RLC',
 'RVT',
 'SHP',
 'SNT',
 'STAC',
 'STORM',
 'VEE',
 'WAND',
 'WAX',
 'WLK',
 'XNK',
 'ZINC']