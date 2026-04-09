const allTeams = ["Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Leeds", "Liverpool", "Man City", "Man Utd", "Newcastle", "Nott'm Forest", "Spurs", "Sunderland", "West Ham", "Wolves"];
const teamPlayersData = {
    "Man City": [
        {
            "name": "Erling Haaland",
            "init": "EH",
            "xg": "0.79",
            "price": "14.6",
            "style": "tg-gold",
            "isSuper": true
        },
        {
            "name": "Antoine Semenyo",
            "init": "AS",
            "xg": "0.35",
            "price": "8.3",
            "style": "tg-silver",
            "isSuper": false
        },
        {
            "name": "Omar Marmoush",
            "init": "OM",
            "xg": "0.35",
            "price": "8.3",
            "style": "tg-bronze",
            "isSuper": false
        },
        {
            "name": "S\u00e1vio Moreira de Oliveira",
            "init": "SO",
            "xg": "0.28",
            "price": "6.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Phil Foden",
            "init": "PF",
            "xg": "0.27",
            "price": "8.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Tijjani Reijnders",
            "init": "TR",
            "xg": "0.24",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Rayan Cherki",
            "init": "RC",
            "xg": "0.18",
            "price": "6.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Nico O'Reilly",
            "init": "NO",
            "xg": "0.17",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Max Alleyne",
            "init": "MA",
            "xg": "0.17",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jo\u0161ko Gvardiol",
            "init": "JG",
            "xg": "0.15",
            "price": "5.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "J\u00e9r\u00e9my Doku",
            "init": "JD",
            "xg": "0.14",
            "price": "6.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Marc Gu\u00e9hi",
            "init": "MG",
            "xg": "0.12",
            "price": "5.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Bernardo Mota Veiga de Carvalho e Silva",
            "init": "BS",
            "xg": "0.07",
            "price": "6.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Rodrigo 'Rodri' Hernandez Cascante",
            "init": "RC",
            "xg": "0.05",
            "price": "6.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Rayan A\u00eft-Nouri",
            "init": "RA",
            "xg": "0.05",
            "price": "5.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Nathan Ak\u00e9",
            "init": "NA",
            "xg": "0.05",
            "price": "5.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Nico Gonz\u00e1lez Iglesias",
            "init": "NI",
            "xg": "0.04",
            "price": "5.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Abdukodir Khusanov",
            "init": "AK",
            "xg": "0.04",
            "price": "5.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "R\u00faben dos Santos Gato Alves Dias",
            "init": "RD",
            "xg": "0.03",
            "price": "5.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Rico Lewis",
            "init": "RL",
            "xg": "0.03",
            "price": "4.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Matheus Nunes",
            "init": "MN",
            "xg": "0.01",
            "price": "5.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Gianluigi Donnarumma",
            "init": "GD",
            "xg": "0.00",
            "price": "5.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "John Stones",
            "init": "JS",
            "xg": "0.00",
            "price": "5.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "James Trafford",
            "init": "JT",
            "xg": "0.00",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Divine Mukasa",
            "init": "DM",
            "xg": "0.00",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Mateo Kova\u010di\u0107",
            "init": "MK",
            "xg": "0.00",
            "price": "5.8",
            "style": "tg-regular",
            "isSuper": false
        }
    ],
    "Man Utd": [
        {
            "name": "Shea Lacey",
            "init": "SL",
            "xg": "0.52",
            "price": "4.5",
            "style": "tg-gold",
            "isSuper": false
        },
        {
            "name": "Benjamin Sesko",
            "init": "BS",
            "xg": "0.49",
            "price": "7.3",
            "style": "tg-silver",
            "isSuper": false
        },
        {
            "name": "Joshua Zirkzee",
            "init": "JZ",
            "xg": "0.39",
            "price": "5.8",
            "style": "tg-bronze",
            "isSuper": false
        },
        {
            "name": "Bruno Borges Fernandes",
            "init": "BF",
            "xg": "0.35",
            "price": "10.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Bryan Mbeumo",
            "init": "BM",
            "xg": "0.34",
            "price": "8.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Matheus Santos Carneiro da Cunha",
            "init": "MC",
            "xg": "0.26",
            "price": "8.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Amad Diallo",
            "init": "AD",
            "xg": "0.21",
            "price": "6.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Carlos Henrique Casimiro",
            "init": "CC",
            "xg": "0.20",
            "price": "5.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Mason Mount",
            "init": "MM",
            "xg": "0.17",
            "price": "5.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Patrick Dorgu",
            "init": "PD",
            "xg": "0.13",
            "price": "4.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Matthijs de Ligt",
            "init": "ML",
            "xg": "0.11",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Diogo Dalot Teixeira",
            "init": "DT",
            "xg": "0.06",
            "price": "4.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Harry Maguire",
            "init": "HM",
            "xg": "0.06",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Leny Yoro",
            "init": "LY",
            "xg": "0.06",
            "price": "4.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Manuel Ugarte Ribeiro",
            "init": "MR",
            "xg": "0.06",
            "price": "4.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ayden Heaven",
            "init": "AH",
            "xg": "0.05",
            "price": "3.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Noussair Mazraoui",
            "init": "NM",
            "xg": "0.03",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jack Fletcher",
            "init": "JF",
            "xg": "0.03",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Luke Shaw",
            "init": "LS",
            "xg": "0.02",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Kobbie Mainoo",
            "init": "KM",
            "xg": "0.02",
            "price": "4.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Lisandro Mart\u00ednez",
            "init": "LM",
            "xg": "0.01",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Senne Lammens",
            "init": "SL",
            "xg": "0.00",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Altay Bay\u0131nd\u0131r",
            "init": "AB",
            "xg": "0.00",
            "price": "4.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Tyrell Malacia",
            "init": "TM",
            "xg": "0.00",
            "price": "3.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Tyler Fredricson",
            "init": "TF",
            "xg": "0.00",
            "price": "3.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Bendito Mantato",
            "init": "BM",
            "xg": "0.00",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Tyler Fletcher",
            "init": "TF",
            "xg": "0.00",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        }
    ],
    "Arsenal": [
        {
            "name": "Max Dowman",
            "init": "MD",
            "xg": "2.32",
            "price": "4.2",
            "style": "tg-gold",
            "isSuper": false
        },
        {
            "name": "Gabriel Fernando de Jesus",
            "init": "GJ",
            "xg": "0.52",
            "price": "6.4",
            "style": "tg-silver",
            "isSuper": false
        },
        {
            "name": "Viktor Gy\u00f6keres",
            "init": "VG",
            "xg": "0.44",
            "price": "8.8",
            "style": "tg-bronze",
            "isSuper": false
        },
        {
            "name": "Gabriel Martinelli Silva",
            "init": "GS",
            "xg": "0.38",
            "price": "6.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Bukayo Saka",
            "init": "BS",
            "xg": "0.32",
            "price": "9.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Leandro Trossard",
            "init": "LT",
            "xg": "0.27",
            "price": "6.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Mikel Merino Zaz\u00f3n",
            "init": "MZ",
            "xg": "0.27",
            "price": "5.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Eberechi Eze",
            "init": "EE",
            "xg": "0.23",
            "price": "7.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Riccardo Calafiori",
            "init": "RC",
            "xg": "0.18",
            "price": "5.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jurri\u00ebn Timber",
            "init": "JT",
            "xg": "0.17",
            "price": "6.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ethan Nwaneri",
            "init": "EN",
            "xg": "0.13",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Declan Rice",
            "init": "DR",
            "xg": "0.11",
            "price": "7.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Kai Havertz",
            "init": "KH",
            "xg": "0.11",
            "price": "7.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Mart\u00edn Zubimendi Ib\u00e1\u00f1ez",
            "init": "MI",
            "xg": "0.10",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Noni Madueke",
            "init": "NM",
            "xg": "0.10",
            "price": "6.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Benjamin White",
            "init": "BW",
            "xg": "0.09",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Gabriel dos Santos Magalh\u00e3es",
            "init": "GM",
            "xg": "0.08",
            "price": "7.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Martin \u00d8degaard",
            "init": "M\u00d8",
            "xg": "0.08",
            "price": "7.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Christian N\u00f8rgaard",
            "init": "CN",
            "xg": "0.08",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "William Saliba",
            "init": "WS",
            "xg": "0.04",
            "price": "6.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Piero Hincapi\u00e9",
            "init": "PH",
            "xg": "0.02",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Myles Lewis-Skelly",
            "init": "ML",
            "xg": "0.01",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "David Raya Mart\u00edn",
            "init": "DM",
            "xg": "0.00",
            "price": "6.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Cristhian Mosquera",
            "init": "CM",
            "xg": "0.00",
            "price": "5.3",
            "style": "tg-regular",
            "isSuper": false
        }
    ],
    "Chelsea": [
        {
            "name": "Cole Palmer",
            "init": "CP",
            "xg": "0.58",
            "price": "10.6",
            "style": "tg-gold",
            "isSuper": false
        },
        {
            "name": "Jo\u00e3o Pedro Junqueira de Jesus",
            "init": "JJ",
            "xg": "0.54",
            "price": "7.7",
            "style": "tg-silver",
            "isSuper": false
        },
        {
            "name": "Marc Guiu Paz",
            "init": "MP",
            "xg": "0.53",
            "price": "4.1",
            "style": "tg-bronze",
            "isSuper": false
        },
        {
            "name": "Liam Delap",
            "init": "LD",
            "xg": "0.46",
            "price": "6.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Enzo Fern\u00e1ndez",
            "init": "EF",
            "xg": "0.36",
            "price": "6.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Mamadou Sarr",
            "init": "MS",
            "xg": "0.35",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Est\u00eav\u00e3o Almeida de Oliveira Gon\u00e7alves",
            "init": "EG",
            "xg": "0.34",
            "price": "6.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Alejandro Garnacho Ferreyra",
            "init": "AF",
            "xg": "0.26",
            "price": "6.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Pedro Lomba Neto",
            "init": "PN",
            "xg": "0.18",
            "price": "7.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Andrey Nascimento dos Santos",
            "init": "AS",
            "xg": "0.16",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jamie Bynoe-Gittens",
            "init": "JB",
            "xg": "0.15",
            "price": "6.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Josh Acheampong",
            "init": "JA",
            "xg": "0.10",
            "price": "3.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Malo Gusto",
            "init": "MG",
            "xg": "0.08",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Marc Cucurella Saseta",
            "init": "MS",
            "xg": "0.07",
            "price": "6.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Trevoh Chalobah",
            "init": "TC",
            "xg": "0.05",
            "price": "5.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Reece James",
            "init": "RJ",
            "xg": "0.05",
            "price": "5.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Mois\u00e9s Caicedo Corozo",
            "init": "MC",
            "xg": "0.05",
            "price": "5.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jorrel Hato",
            "init": "JH",
            "xg": "0.05",
            "price": "4.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Wesley Fofana",
            "init": "WF",
            "xg": "0.04",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Tosin Adarabioyo",
            "init": "TA",
            "xg": "0.01",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Robert Lynch S\u00e1nchez",
            "init": "RS",
            "xg": "0.00",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Beno\u00eet Badiashile Mukinayi",
            "init": "BM",
            "xg": "0.00",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Rom\u00e9o Lavia",
            "init": "RL",
            "xg": "0.00",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Filip J\u00f6rgensen",
            "init": "FJ",
            "xg": "0.00",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        }
    ],
    "Brentford": [
        {
            "name": "Reiss Nelson",
            "init": "RN",
            "xg": "1.10",
            "price": "4.8",
            "style": "tg-gold",
            "isSuper": false
        },
        {
            "name": "F\u00e1bio Freitas Gouveia Carvalho",
            "init": "FC",
            "xg": "0.63",
            "price": "4.7",
            "style": "tg-silver",
            "isSuper": false
        },
        {
            "name": "Igor Thiago Nascimento Rodrigues",
            "init": "IR",
            "xg": "0.57",
            "price": "7.2",
            "style": "tg-bronze",
            "isSuper": false
        },
        {
            "name": "Kevin Schade",
            "init": "KS",
            "xg": "0.42",
            "price": "6.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Dango Ouattara",
            "init": "DO",
            "xg": "0.30",
            "price": "6.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Romelle Donovan",
            "init": "RD",
            "xg": "0.21",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Keane Lewis-Potter",
            "init": "KL",
            "xg": "0.16",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Sepp van den Berg",
            "init": "SB",
            "xg": "0.12",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Mathias Jensen",
            "init": "MJ",
            "xg": "0.12",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Mikkel Damsgaard",
            "init": "MD",
            "xg": "0.11",
            "price": "5.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Nathan Collins",
            "init": "NC",
            "xg": "0.07",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Vitaly Janelt",
            "init": "VJ",
            "xg": "0.06",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Aaron Hickey",
            "init": "AH",
            "xg": "0.06",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Yehor Yarmoliuk",
            "init": "YY",
            "xg": "0.05",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Kristoffer Ajer",
            "init": "KA",
            "xg": "0.04",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jordan Henderson",
            "init": "JH",
            "xg": "0.02",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Michael Kayode",
            "init": "MK",
            "xg": "0.01",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Rico Henry",
            "init": "RH",
            "xg": "0.01",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Caoimh\u00edn Kelleher",
            "init": "CK",
            "xg": "0.00",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Frank Onyeka",
            "init": "FO",
            "xg": "0.00",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ethan Pinnock",
            "init": "EP",
            "xg": "0.00",
            "price": "4.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "H\u00e1kon Rafn Valdimarsson",
            "init": "HV",
            "xg": "0.00",
            "price": "3.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Antoni Milambo",
            "init": "AM",
            "xg": "0.00",
            "price": "5.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Myles Peart-Harris",
            "init": "MP",
            "xg": "0.00",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        }
    ],
    "Fulham": [
        {
            "name": "Ra\u00fal Jim\u00e9nez Rodr\u00edguez",
            "init": "RR",
            "xg": "0.47",
            "price": "6.2",
            "style": "tg-gold",
            "isSuper": false
        },
        {
            "name": "Emile Smith Rowe",
            "init": "ER",
            "xg": "0.26",
            "price": "5.6",
            "style": "tg-silver",
            "isSuper": false
        },
        {
            "name": "Rodrigo Muniz Carvalho",
            "init": "RC",
            "xg": "0.24",
            "price": "5.3",
            "style": "tg-bronze",
            "isSuper": false
        },
        {
            "name": "Harry Wilson",
            "init": "HW",
            "xg": "0.20",
            "price": "6.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Samuel Chukwueze",
            "init": "SC",
            "xg": "0.19",
            "price": "5.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Josh King",
            "init": "JK",
            "xg": "0.17",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Tom Cairney",
            "init": "TC",
            "xg": "0.16",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Harrison Reed",
            "init": "HR",
            "xg": "0.16",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Sa\u0161a Luki\u0107",
            "init": "SL",
            "xg": "0.13",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Kevin Santos Lopes de Macedo",
            "init": "KM",
            "xg": "0.11",
            "price": "5.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Timothy Castagne",
            "init": "TC",
            "xg": "0.09",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ryan Sessegnon",
            "init": "RS",
            "xg": "0.07",
            "price": "5.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Alex Iwobi",
            "init": "AI",
            "xg": "0.06",
            "price": "6.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Calvin Bassey",
            "init": "CB",
            "xg": "0.06",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Oscar Bobb",
            "init": "OB",
            "xg": "0.06",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Joachim Andersen",
            "init": "JA",
            "xg": "0.05",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Kenny Tete",
            "init": "KT",
            "xg": "0.05",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Sander Berge",
            "init": "SB",
            "xg": "0.05",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Antonee Robinson",
            "init": "AR",
            "xg": "0.02",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Bernd Leno",
            "init": "BL",
            "xg": "0.00",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jorge Cuenca Barreno",
            "init": "JB",
            "xg": "0.00",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Issa Diop",
            "init": "ID",
            "xg": "0.00",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jonah Kusi-Asare",
            "init": "JK",
            "xg": "0.00",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        }
    ],
    "West Ham": [
        {
            "name": "Callum Wilson",
            "init": "CW",
            "xg": "0.59",
            "price": "5.8",
            "style": "tg-gold",
            "isSuper": false
        },
        {
            "name": "Valent\u00edn Castellanos",
            "init": "VC",
            "xg": "0.27",
            "price": "5.5",
            "style": "tg-silver",
            "isSuper": false
        },
        {
            "name": "Tom\u00e1\u0161 Sou\u010dek",
            "init": "TS",
            "xg": "0.26",
            "price": "5.7",
            "style": "tg-bronze",
            "isSuper": false
        },
        {
            "name": "Crysencio Summerville",
            "init": "CS",
            "xg": "0.22",
            "price": "5.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Niclas F\u00fcllkrug",
            "init": "NF",
            "xg": "0.21",
            "price": "5.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jarrod Bowen",
            "init": "JB",
            "xg": "0.20",
            "price": "7.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Callum Marshall",
            "init": "CM",
            "xg": "0.20",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Lucas Tolentino Coelho de Lima",
            "init": "LL",
            "xg": "0.17",
            "price": "5.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Axel Disasi",
            "init": "AD",
            "xg": "0.12",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Kyle Walker-Peters",
            "init": "KW",
            "xg": "0.11",
            "price": "4.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Mohamadou Kant\u00e9",
            "init": "MK",
            "xg": "0.11",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Adama Traor\u00e9 Diarra",
            "init": "AD",
            "xg": "0.10",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Pablo Felipe Pereira de Jesus",
            "init": "PJ",
            "xg": "0.10",
            "price": "5.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ezra Mayers",
            "init": "EM",
            "xg": "0.10",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Konstantinos Mavropanos",
            "init": "KM",
            "xg": "0.09",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Mateus Gon\u00e7alo Espanha Fernandes",
            "init": "MF",
            "xg": "0.05",
            "price": "5.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Luis Guilherme Lira dos Santos",
            "init": "LS",
            "xg": "0.05",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Nayef Aguerd",
            "init": "NA",
            "xg": "0.05",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Soungoutou Magassa",
            "init": "SM",
            "xg": "0.04",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Maximilian Kilman",
            "init": "MK",
            "xg": "0.03",
            "price": "4.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "El Hadji Malick Diouf",
            "init": "ED",
            "xg": "0.02",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Freddie Potts",
            "init": "FP",
            "xg": "0.02",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ollie Scarles",
            "init": "OS",
            "xg": "0.02",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Guido Rodr\u00edguez",
            "init": "GR",
            "xg": "0.02",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jean-Clair Todibo",
            "init": "JT",
            "xg": "0.01",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Aaron Wan-Bissaka",
            "init": "AW",
            "xg": "0.00",
            "price": "4.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Alphonse Areola",
            "init": "AA",
            "xg": "0.00",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Mads Hermansen",
            "init": "MH",
            "xg": "0.00",
            "price": "4.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Andy Irving",
            "init": "AI",
            "xg": "0.00",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "George Earthy",
            "init": "GE",
            "xg": "0.00",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        }
    ],
    "Bournemouth": [
        {
            "name": "Enes \u00dcnal",
            "init": "E\u00dc",
            "xg": "0.96",
            "price": "5.4",
            "style": "tg-gold",
            "isSuper": false
        },
        {
            "name": "David Brooks",
            "init": "DB",
            "xg": "0.43",
            "price": "5.0",
            "style": "tg-silver",
            "isSuper": false
        },
        {
            "name": "Junior Kroupi",
            "init": "JK",
            "xg": "0.40",
            "price": "4.7",
            "style": "tg-bronze",
            "isSuper": false
        },
        {
            "name": "Francisco Evanilson de Lima Barbosa",
            "init": "FB",
            "xg": "0.35",
            "price": "6.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Marcus Tavernier",
            "init": "MT",
            "xg": "0.31",
            "price": "5.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Amine Adli",
            "init": "AA",
            "xg": "0.24",
            "price": "5.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Justin Kluivert",
            "init": "JK",
            "xg": "0.22",
            "price": "6.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ryan Christie",
            "init": "RC",
            "xg": "0.21",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Rayan Vitor Simpl\u00edcio Rocha",
            "init": "RR",
            "xg": "0.15",
            "price": "5.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ben Gannon-Doak",
            "init": "BG",
            "xg": "0.15",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Alex Scott",
            "init": "AS",
            "xg": "0.13",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Alex T\u00f3th",
            "init": "AT",
            "xg": "0.08",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Marcos Senesi Bar\u00f3n",
            "init": "MB",
            "xg": "0.05",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "\u00c1lex Jim\u00e9nez S\u00e1nchez",
            "init": "\u00c1S",
            "xg": "0.05",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "James Hill",
            "init": "JH",
            "xg": "0.04",
            "price": "4.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Tyler Adams",
            "init": "TA",
            "xg": "0.04",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Veljko Milosavljevic",
            "init": "VM",
            "xg": "0.04",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Adrien Truffert",
            "init": "AT",
            "xg": "0.01",
            "price": "4.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Lewis Cook",
            "init": "LC",
            "xg": "0.01",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "\u0110or\u0111e Petrovi\u0107",
            "init": "\u0110P",
            "xg": "0.00",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Bafod\u00e9 Diakit\u00e9",
            "init": "BD",
            "xg": "0.00",
            "price": "4.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Adam Smith",
            "init": "AS",
            "xg": "0.00",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Hamed Traor\u00e8",
            "init": "HT",
            "xg": "0.00",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Julio Soler Barreto",
            "init": "JB",
            "xg": "0.00",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ben Winterburn",
            "init": "BW",
            "xg": "0.00",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        }
    ],
    "Everton": [
        {
            "name": "Norberto Bercique Gomes Betuncal",
            "init": "NB",
            "xg": "0.53",
            "price": "5.0",
            "style": "tg-gold",
            "isSuper": false
        },
        {
            "name": "Thierno Barry",
            "init": "TB",
            "xg": "0.34",
            "price": "5.7",
            "style": "tg-silver",
            "isSuper": false
        },
        {
            "name": "Iliman Ndiaye",
            "init": "IN",
            "xg": "0.21",
            "price": "6.2",
            "style": "tg-bronze",
            "isSuper": false
        },
        {
            "name": "Tyrique George",
            "init": "TG",
            "xg": "0.17",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Kiernan Dewsbury-Hall",
            "init": "KD",
            "xg": "0.15",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Carlos Alcaraz Dur\u00e1n",
            "init": "CD",
            "xg": "0.14",
            "price": "5.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Harrison Armstrong",
            "init": "HA",
            "xg": "0.14",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Merlin R\u00f6hl",
            "init": "MR",
            "xg": "0.13",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jack Grealish",
            "init": "JG",
            "xg": "0.11",
            "price": "6.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Dwight McNeil",
            "init": "DM",
            "xg": "0.11",
            "price": "5.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Michael Keane",
            "init": "MK",
            "xg": "0.09",
            "price": "4.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Idrissa Gana Gueye",
            "init": "IG",
            "xg": "0.08",
            "price": "5.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "James Tarkowski",
            "init": "JT",
            "xg": "0.07",
            "price": "5.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "James Garner",
            "init": "JG",
            "xg": "0.06",
            "price": "5.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jarrad Branthwaite",
            "init": "JB",
            "xg": "0.05",
            "price": "5.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Tyler Dibling",
            "init": "TD",
            "xg": "0.05",
            "price": "5.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jake O'Brien",
            "init": "JO",
            "xg": "0.03",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Tim Iroegbunam",
            "init": "TI",
            "xg": "0.03",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Vitalii Mykolenko",
            "init": "VM",
            "xg": "0.01",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Nathan Patterson",
            "init": "NP",
            "xg": "0.01",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jordan Pickford",
            "init": "JP",
            "xg": "0.00",
            "price": "5.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "S\u00e9amus Coleman",
            "init": "SC",
            "xg": "0.00",
            "price": "4.2",
            "style": "tg-regular",
            "isSuper": false
        }
    ],
    "Newcastle": [
        {
            "name": "Anthony Gordon",
            "init": "AG",
            "xg": "0.45",
            "price": "7.2",
            "style": "tg-gold",
            "isSuper": false
        },
        {
            "name": "Yoane Wissa",
            "init": "YW",
            "xg": "0.42",
            "price": "7.3",
            "style": "tg-silver",
            "isSuper": false
        },
        {
            "name": "Nick Woltemade",
            "init": "NW",
            "xg": "0.35",
            "price": "6.7",
            "style": "tg-bronze",
            "isSuper": false
        },
        {
            "name": "Harvey Barnes",
            "init": "HB",
            "xg": "0.34",
            "price": "6.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "William Osula",
            "init": "WO",
            "xg": "0.23",
            "price": "5.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Bruno Guimar\u00e3es Rodriguez Moura",
            "init": "BM",
            "xg": "0.21",
            "price": "6.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jacob Murphy",
            "init": "JM",
            "xg": "0.21",
            "price": "5.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jamaal Lascelles",
            "init": "JL",
            "xg": "0.19",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Malick Thiaw",
            "init": "MT",
            "xg": "0.15",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Joelinton C\u00e1ssio Apolin\u00e1rio de Lira",
            "init": "JL",
            "xg": "0.11",
            "price": "5.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Lewis Miley",
            "init": "LM",
            "xg": "0.11",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Anthony Elanga",
            "init": "AE",
            "xg": "0.11",
            "price": "6.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Joe Willock",
            "init": "JW",
            "xg": "0.11",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Sven Botman",
            "init": "SB",
            "xg": "0.10",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jacob Ramsey",
            "init": "JR",
            "xg": "0.09",
            "price": "5.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Fabian Sch\u00e4r",
            "init": "FS",
            "xg": "0.08",
            "price": "5.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Sandro Tonali",
            "init": "ST",
            "xg": "0.07",
            "price": "5.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Lewis Hall",
            "init": "LH",
            "xg": "0.04",
            "price": "5.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Nick Pope",
            "init": "NP",
            "xg": "0.01",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Dan Burn",
            "init": "DB",
            "xg": "0.01",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Tino Livramento",
            "init": "TL",
            "xg": "0.01",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Kieran Trippier",
            "init": "KT",
            "xg": "0.01",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Aaron Ramsdale",
            "init": "AR",
            "xg": "0.00",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Alex Murphy",
            "init": "AM",
            "xg": "0.00",
            "price": "3.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Emil Krafth",
            "init": "EK",
            "xg": "0.00",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        }
    ],
    "Nott'm Forest": [
        {
            "name": "Taiwo Awoniyi",
            "init": "TA",
            "xg": "0.55",
            "price": "5.2",
            "style": "tg-gold",
            "isSuper": false
        },
        {
            "name": "Lorenzo Lucca",
            "init": "LL",
            "xg": "0.54",
            "price": "5.5",
            "style": "tg-silver",
            "isSuper": false
        },
        {
            "name": "Chris Wood",
            "init": "CW",
            "xg": "0.47",
            "price": "7.1",
            "style": "tg-bronze",
            "isSuper": false
        },
        {
            "name": "Arnaud Kalimuendo",
            "init": "AK",
            "xg": "0.44",
            "price": "6.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Morgan Gibbs-White",
            "init": "MG",
            "xg": "0.27",
            "price": "7.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Igor Jesus Maciel da Cruz",
            "init": "IC",
            "xg": "0.23",
            "price": "5.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Callum Hudson-Odoi",
            "init": "CH",
            "xg": "0.14",
            "price": "5.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Omari Hutchinson",
            "init": "OH",
            "xg": "0.13",
            "price": "5.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Dilane Bakwa",
            "init": "DB",
            "xg": "0.13",
            "price": "5.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Nicol\u00f2 Savona",
            "init": "NS",
            "xg": "0.12",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Nicol\u00e1s Dom\u00ednguez",
            "init": "ND",
            "xg": "0.11",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Elliot Anderson",
            "init": "EA",
            "xg": "0.09",
            "price": "5.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Dan Ndoye",
            "init": "DN",
            "xg": "0.08",
            "price": "5.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Felipe Rodrigues da Silva",
            "init": "FS",
            "xg": "0.08",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Neco Williams",
            "init": "NW",
            "xg": "0.06",
            "price": "4.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ibrahim Sangar\u00e9",
            "init": "IS",
            "xg": "0.06",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jair Paula da Cunha Filho",
            "init": "JF",
            "xg": "0.06",
            "price": "4.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ryan Yates",
            "init": "RY",
            "xg": "0.05",
            "price": "4.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Nikola Milenkovi\u0107",
            "init": "NM",
            "xg": "0.03",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Murillo Costa dos Santos",
            "init": "MS",
            "xg": "0.03",
            "price": "5.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ola Aina",
            "init": "OA",
            "xg": "0.02",
            "price": "4.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Oleksandr Zinchenko",
            "init": "OZ",
            "xg": "0.02",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "James McAtee",
            "init": "JM",
            "xg": "0.01",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Matz Sels",
            "init": "MS",
            "xg": "0.00",
            "price": "4.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Stefan Ortega Moreno",
            "init": "SM",
            "xg": "0.00",
            "price": "4.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "John Victor Maciel Furtado",
            "init": "JF",
            "xg": "0.00",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Zach Abbott",
            "init": "ZA",
            "xg": "0.00",
            "price": "3.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Luca Netz",
            "init": "LN",
            "xg": "0.00",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jo\u00e3o Pedro Ferreira da Silva",
            "init": "JS",
            "xg": "0.00",
            "price": "5.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Angus Gunn",
            "init": "AG",
            "xg": "0.00",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        }
    ],
    "Aston Villa": [
        {
            "name": "Tammy Abraham",
            "init": "TA",
            "xg": "0.58",
            "price": "6.0",
            "style": "tg-gold",
            "isSuper": false
        },
        {
            "name": "Donyell Malen",
            "init": "DM",
            "xg": "0.57",
            "price": "5.1",
            "style": "tg-silver",
            "isSuper": false
        },
        {
            "name": "Ollie Watkins",
            "init": "OW",
            "xg": "0.41",
            "price": "8.5",
            "style": "tg-bronze",
            "isSuper": false
        },
        {
            "name": "Harvey Elliott",
            "init": "HE",
            "xg": "0.24",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ross Barkley",
            "init": "RB",
            "xg": "0.19",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Morgan Rogers",
            "init": "MR",
            "xg": "0.18",
            "price": "7.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Emiliano Buend\u00eda Stati",
            "init": "ES",
            "xg": "0.18",
            "price": "5.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "John McGinn",
            "init": "JM",
            "xg": "0.14",
            "price": "5.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "George Hemmings",
            "init": "GH",
            "xg": "0.14",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Alysson Edward Franco da Rocha dos Santos",
            "init": "AS",
            "xg": "0.10",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Tyrone Mings",
            "init": "TM",
            "xg": "0.09",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Leon Bailey",
            "init": "LB",
            "xg": "0.09",
            "price": "5.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Amadou Onana",
            "init": "AO",
            "xg": "0.08",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ian Maatsen",
            "init": "IM",
            "xg": "0.08",
            "price": "4.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jadon Sancho",
            "init": "JS",
            "xg": "0.08",
            "price": "5.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Youri Tielemans",
            "init": "YT",
            "xg": "0.07",
            "price": "5.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Douglas Luiz Soares de Paulo",
            "init": "DP",
            "xg": "0.06",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Matty Cash",
            "init": "MC",
            "xg": "0.04",
            "price": "4.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ezri Konsa Ngoyo",
            "init": "EN",
            "xg": "0.04",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Pau Torres",
            "init": "PT",
            "xg": "0.04",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Lucas Digne",
            "init": "LD",
            "xg": "0.03",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Boubacar Kamara",
            "init": "BK",
            "xg": "0.03",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Emiliano Mart\u00ednez Romero",
            "init": "ER",
            "xg": "0.00",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Lamare Bogarde",
            "init": "LB",
            "xg": "0.00",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Victor Lindel\u00f6f",
            "init": "VL",
            "xg": "0.00",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Marco Bizot",
            "init": "MB",
            "xg": "0.00",
            "price": "4.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Andr\u00e9s Garc\u00eda",
            "init": "AG",
            "xg": "0.00",
            "price": "3.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jamaldeen Jimoh-Aloba",
            "init": "JJ",
            "xg": "0.00",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Bradley Burrowes",
            "init": "BB",
            "xg": "0.00",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        }
    ],
    "Liverpool": [
        {
            "name": "Trey Nyoni",
            "init": "TN",
            "xg": "2.56",
            "price": "4.3",
            "style": "tg-gold",
            "isSuper": false
        },
        {
            "name": "Hugo Ekitik\u00e9",
            "init": "HE",
            "xg": "0.51",
            "price": "9.2",
            "style": "tg-silver",
            "isSuper": false
        },
        {
            "name": "Federico Chiesa",
            "init": "FC",
            "xg": "0.44",
            "price": "6.3",
            "style": "tg-bronze",
            "isSuper": false
        },
        {
            "name": "Rio Ngumoha",
            "init": "RN",
            "xg": "0.38",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Alexander Isak",
            "init": "AI",
            "xg": "0.37",
            "price": "10.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Mohamed Salah",
            "init": "MS",
            "xg": "0.34",
            "price": "14.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Cody Gakpo",
            "init": "CG",
            "xg": "0.29",
            "price": "7.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Florian Wirtz",
            "init": "FW",
            "xg": "0.27",
            "price": "8.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Alexis Mac Allister",
            "init": "AA",
            "xg": "0.14",
            "price": "6.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Dominik Szoboszlai",
            "init": "DS",
            "xg": "0.13",
            "price": "7.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Curtis Jones",
            "init": "CJ",
            "xg": "0.10",
            "price": "5.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Virgil van Dijk",
            "init": "VD",
            "xg": "0.09",
            "price": "6.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ryan Gravenberch",
            "init": "RG",
            "xg": "0.06",
            "price": "5.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jeremie Frimpong",
            "init": "JF",
            "xg": "0.06",
            "price": "5.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ibrahima Konat\u00e9",
            "init": "IK",
            "xg": "0.04",
            "price": "5.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Milos Kerkez",
            "init": "MK",
            "xg": "0.04",
            "price": "5.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Andrew Robertson",
            "init": "AR",
            "xg": "0.04",
            "price": "5.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Joe Gomez",
            "init": "JG",
            "xg": "0.04",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Conor Bradley",
            "init": "CB",
            "xg": "0.02",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Endo Wataru",
            "init": "EW",
            "xg": "0.02",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Alisson Becker",
            "init": "AB",
            "xg": "0.00",
            "price": "5.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Giorgi Mamardashvili",
            "init": "GM",
            "xg": "0.00",
            "price": "4.1",
            "style": "tg-regular",
            "isSuper": false
        }
    ],
    "Crystal Palace": [
        {
            "name": "Jean-Philippe Mateta",
            "init": "JM",
            "xg": "0.56",
            "price": "7.5",
            "style": "tg-gold",
            "isSuper": false
        },
        {
            "name": "Isma\u00efla Sarr",
            "init": "IS",
            "xg": "0.42",
            "price": "6.3",
            "style": "tg-silver",
            "isSuper": false
        },
        {
            "name": "Eddie Nketiah",
            "init": "EN",
            "xg": "0.38",
            "price": "5.4",
            "style": "tg-bronze",
            "isSuper": false
        },
        {
            "name": "Justin Devenny",
            "init": "JD",
            "xg": "0.36",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Christantus Uche",
            "init": "CU",
            "xg": "0.28",
            "price": "5.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Y\u00e9remy Pino Santos",
            "init": "YS",
            "xg": "0.21",
            "price": "5.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "J\u00f8rgen Strand Larsen",
            "init": "JL",
            "xg": "0.20",
            "price": "6.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Evann Guessand",
            "init": "EG",
            "xg": "0.16",
            "price": "6.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Brennan Johnson",
            "init": "BJ",
            "xg": "0.14",
            "price": "6.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Daniel Mu\u00f1oz Mej\u00eda",
            "init": "DM",
            "xg": "0.10",
            "price": "5.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jaydee Canvot",
            "init": "JC",
            "xg": "0.10",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Daichi Kamada",
            "init": "DK",
            "xg": "0.09",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Maxence Lacroix",
            "init": "ML",
            "xg": "0.08",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jefferson Lerma Sol\u00eds",
            "init": "JS",
            "xg": "0.08",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Will Hughes",
            "init": "WH",
            "xg": "0.08",
            "price": "4.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Nathaniel Clyne",
            "init": "NC",
            "xg": "0.08",
            "price": "3.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Adam Wharton",
            "init": "AW",
            "xg": "0.05",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Tyrick Mitchell",
            "init": "TM",
            "xg": "0.04",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Chris Richards",
            "init": "CR",
            "xg": "0.04",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Chadi Riad Dnanou",
            "init": "CD",
            "xg": "0.03",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Dean Henderson",
            "init": "DH",
            "xg": "0.00",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Walter Ben\u00edtez",
            "init": "WB",
            "xg": "0.00",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Borna Sosa",
            "init": "BS",
            "xg": "0.00",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Romain Esse",
            "init": "RE",
            "xg": "0.00",
            "price": "4.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jo\u00e9l Drakes-Thomas",
            "init": "JD",
            "xg": "0.00",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Kaden Rodney",
            "init": "KR",
            "xg": "0.00",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Odsonne \u00c9douard",
            "init": "O\u00c9",
            "xg": "0.00",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        }
    ],
    "Leeds": [
        {
            "name": "Lukas Nmecha",
            "init": "LN",
            "xg": "0.70",
            "price": "5.0",
            "style": "tg-gold",
            "isSuper": false
        },
        {
            "name": "Dominic Calvert-Lewin",
            "init": "DC",
            "xg": "0.50",
            "price": "5.7",
            "style": "tg-silver",
            "isSuper": false
        },
        {
            "name": "Jo\u00ebl Piroe",
            "init": "JP",
            "xg": "0.34",
            "price": "4.9",
            "style": "tg-bronze",
            "isSuper": false
        },
        {
            "name": "Noah Okafor",
            "init": "NO",
            "xg": "0.30",
            "price": "5.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Brenden Aaronson",
            "init": "BA",
            "xg": "0.19",
            "price": "5.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Daniel James",
            "init": "DJ",
            "xg": "0.16",
            "price": "5.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Anton Stach",
            "init": "AS",
            "xg": "0.11",
            "price": "4.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Pascal Struijk",
            "init": "PS",
            "xg": "0.10",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Tanaka Ao",
            "init": "TA",
            "xg": "0.10",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jack Harrison",
            "init": "JH",
            "xg": "0.10",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jayden Bogle",
            "init": "JB",
            "xg": "0.08",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Sean Longstaff",
            "init": "SL",
            "xg": "0.08",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ethan Ampadu",
            "init": "EA",
            "xg": "0.07",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "James Justin",
            "init": "JJ",
            "xg": "0.07",
            "price": "3.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Wilfried Gnonto",
            "init": "WG",
            "xg": "0.07",
            "price": "5.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jaka Bijol",
            "init": "JB",
            "xg": "0.06",
            "price": "3.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Facundo Buonanotte",
            "init": "FB",
            "xg": "0.05",
            "price": "4.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Joe Rodon",
            "init": "JR",
            "xg": "0.04",
            "price": "3.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Gabriel Gudmundsson",
            "init": "GG",
            "xg": "0.04",
            "price": "3.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ilia Gruev",
            "init": "IG",
            "xg": "0.03",
            "price": "4.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Lucas Estella Perri",
            "init": "LP",
            "xg": "0.00",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Karl Darlow",
            "init": "KD",
            "xg": "0.00",
            "price": "3.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Sebastiaan Bornauw",
            "init": "SB",
            "xg": "0.00",
            "price": "3.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Sam Byram",
            "init": "SB",
            "xg": "0.00",
            "price": "3.7",
            "style": "tg-regular",
            "isSuper": false
        }
    ],
    "Sunderland": [
        {
            "name": "Wilson Isidor",
            "init": "WI",
            "xg": "0.32",
            "price": "5.1",
            "style": "tg-gold",
            "isSuper": false
        },
        {
            "name": "Eliezer Mayenda Dossou",
            "init": "ED",
            "xg": "0.26",
            "price": "5.2",
            "style": "tg-silver",
            "isSuper": false
        },
        {
            "name": "Romaine Mundle",
            "init": "RM",
            "xg": "0.20",
            "price": "4.9",
            "style": "tg-bronze",
            "isSuper": false
        },
        {
            "name": "Brian Brobbey",
            "init": "BB",
            "xg": "0.19",
            "price": "5.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Enzo Le F\u00e9e",
            "init": "EF",
            "xg": "0.18",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Habib Diarra",
            "init": "HD",
            "xg": "0.18",
            "price": "5.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Nilson Angulo",
            "init": "NA",
            "xg": "0.17",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Daniel Ballard",
            "init": "DB",
            "xg": "0.11",
            "price": "4.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Chemsdine Talbi",
            "init": "CT",
            "xg": "0.11",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Patrick Roberts",
            "init": "PR",
            "xg": "0.10",
            "price": "5.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Chris Rigg",
            "init": "CR",
            "xg": "0.08",
            "price": "4.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Bertrand Traor\u00e9",
            "init": "BT",
            "xg": "0.07",
            "price": "5.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Trai Hume",
            "init": "TH",
            "xg": "0.06",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Omar Alderete",
            "init": "OA",
            "xg": "0.05",
            "price": "4.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Simon Adingra",
            "init": "SA",
            "xg": "0.05",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Arthur Masuaku",
            "init": "AM",
            "xg": "0.05",
            "price": "3.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Nordi Mukiele",
            "init": "NM",
            "xg": "0.04",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Granit Xhaka",
            "init": "GX",
            "xg": "0.03",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Lutsharel Geertruida",
            "init": "LG",
            "xg": "0.03",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Noah Sadiki",
            "init": "NS",
            "xg": "0.02",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Dennis Cirkin",
            "init": "DC",
            "xg": "0.02",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Reinildo Mandava",
            "init": "RM",
            "xg": "0.01",
            "price": "3.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Robin Roefs",
            "init": "RR",
            "xg": "0.00",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Melker Ellborg",
            "init": "ME",
            "xg": "0.00",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Luke O'Nien",
            "init": "LO",
            "xg": "0.00",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Dan Neil",
            "init": "DN",
            "xg": "0.00",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jenson Seelt",
            "init": "JS",
            "xg": "0.00",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Djiamgone Jocelin Ta Bi",
            "init": "DB",
            "xg": "0.00",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        }
    ],
    "Brighton": [
        {
            "name": "Matt O'Riley",
            "init": "MO",
            "xg": "0.59",
            "price": "5.5",
            "style": "tg-gold",
            "isSuper": false
        },
        {
            "name": "Charalampos Kostoulas",
            "init": "CK",
            "xg": "0.52",
            "price": "4.8",
            "style": "tg-silver",
            "isSuper": false
        },
        {
            "name": "Danny Welbeck",
            "init": "DW",
            "xg": "0.48",
            "price": "6.1",
            "style": "tg-bronze",
            "isSuper": false
        },
        {
            "name": "Stefanos Tzimas",
            "init": "ST",
            "xg": "0.30",
            "price": "5.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Diego G\u00f3mez Amarilla",
            "init": "DA",
            "xg": "0.24",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Brajan Gruda",
            "init": "BG",
            "xg": "0.24",
            "price": "5.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Mitoma Kaoru",
            "init": "MK",
            "xg": "0.20",
            "price": "6.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jack Hinshelwood",
            "init": "JH",
            "xg": "0.18",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Yankuba Minteh",
            "init": "YM",
            "xg": "0.15",
            "price": "5.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "James Milner",
            "init": "JM",
            "xg": "0.14",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Yasin Ayari",
            "init": "YA",
            "xg": "0.13",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Georginio Rutter",
            "init": "GR",
            "xg": "0.13",
            "price": "5.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Maxim De Cuyper",
            "init": "MC",
            "xg": "0.12",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jo\u00ebl Veltman",
            "init": "JV",
            "xg": "0.11",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Mats Wieffer",
            "init": "MW",
            "xg": "0.09",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jan Paul van Hecke",
            "init": "JH",
            "xg": "0.08",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Pascal Gro\u00df",
            "init": "PG",
            "xg": "0.08",
            "price": "5.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ferdi Kad\u0131o\u011flu",
            "init": "FK",
            "xg": "0.06",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Tom Watson",
            "init": "TW",
            "xg": "0.06",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Lewis Dunk",
            "init": "LD",
            "xg": "0.05",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Carlos Baleba",
            "init": "CB",
            "xg": "0.04",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Olivier Boscagli",
            "init": "OB",
            "xg": "0.01",
            "price": "4.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Bart Verbruggen",
            "init": "BV",
            "xg": "0.00",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Diego Coppola",
            "init": "DC",
            "xg": "0.00",
            "price": "4.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Igor Julio dos Santos de Paulo",
            "init": "IP",
            "xg": "0.00",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Harry Howell",
            "init": "HH",
            "xg": "0.00",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Solly March",
            "init": "SM",
            "xg": "0.00",
            "price": "5.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Joe Knight",
            "init": "JK",
            "xg": "0.00",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Nehemiah Oriola",
            "init": "NO",
            "xg": "0.00",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        }
    ],
    "Burnley": [
        {
            "name": "Zian Flemming",
            "init": "ZF",
            "xg": "0.43",
            "price": "5.3",
            "style": "tg-gold",
            "isSuper": false
        },
        {
            "name": "Ashley Barnes",
            "init": "AB",
            "xg": "0.43",
            "price": "4.2",
            "style": "tg-silver",
            "isSuper": false
        },
        {
            "name": "Oliver Sonne",
            "init": "OS",
            "xg": "0.30",
            "price": "3.8",
            "style": "tg-bronze",
            "isSuper": false
        },
        {
            "name": "Armando Broja",
            "init": "AB",
            "xg": "0.24",
            "price": "5.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Lyle Foster",
            "init": "LF",
            "xg": "0.23",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jaidon Anthony",
            "init": "JA",
            "xg": "0.17",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Marcus Edwards",
            "init": "ME",
            "xg": "0.15",
            "price": "4.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jacob Bruun Larsen",
            "init": "JL",
            "xg": "0.13",
            "price": "5.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Lesley Ugochukwu",
            "init": "LU",
            "xg": "0.11",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Loum Tchaouna",
            "init": "LT",
            "xg": "0.09",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Josh Cullen",
            "init": "JC",
            "xg": "0.06",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Axel Tuanzebe",
            "init": "AT",
            "xg": "0.06",
            "price": "3.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Hannibal Mejbri",
            "init": "HM",
            "xg": "0.05",
            "price": "4.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Josh Laurent",
            "init": "JL",
            "xg": "0.04",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Maxime Est\u00e8ve",
            "init": "ME",
            "xg": "0.03",
            "price": "3.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Florentino Ibrain Morris Lu\u00eds",
            "init": "FL",
            "xg": "0.03",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Bashir Humphreys",
            "init": "BH",
            "xg": "0.03",
            "price": "3.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Lucas Pires Silva",
            "init": "LS",
            "xg": "0.03",
            "price": "3.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Hjalmar Ekdal",
            "init": "HE",
            "xg": "0.02",
            "price": "3.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "James Ward-Prowse",
            "init": "JW",
            "xg": "0.02",
            "price": "5.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Quilindschy Hartman",
            "init": "QH",
            "xg": "0.01",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Joe Worrall",
            "init": "JW",
            "xg": "0.01",
            "price": "3.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Martin D\u00fabravka",
            "init": "MD",
            "xg": "0.00",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Kyle Walker",
            "init": "KW",
            "xg": "0.00",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Mike Tr\u00e9sor Ndayishimiye",
            "init": "MN",
            "xg": "0.00",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jaydon Banel",
            "init": "JB",
            "xg": "0.00",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        }
    ],
    "Spurs": [
        {
            "name": "Richarlison de Andrade",
            "init": "RA",
            "xg": "0.39",
            "price": "6.3",
            "style": "tg-gold",
            "isSuper": false
        },
        {
            "name": "Ben Davies",
            "init": "BD",
            "xg": "0.32",
            "price": "4.3",
            "style": "tg-silver",
            "isSuper": false
        },
        {
            "name": "Dominic Solanke-Mitchell",
            "init": "DS",
            "xg": "0.28",
            "price": "7.2",
            "style": "tg-bronze",
            "isSuper": false
        },
        {
            "name": "Mathys Tel",
            "init": "MT",
            "xg": "0.21",
            "price": "6.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Wilson Odobert",
            "init": "WO",
            "xg": "0.18",
            "price": "5.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Xavi Simons",
            "init": "XS",
            "xg": "0.13",
            "price": "6.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Randal Kolo Muani",
            "init": "RM",
            "xg": "0.12",
            "price": "6.9",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Micky van de Ven",
            "init": "MV",
            "xg": "0.11",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Mohammed Kudus",
            "init": "MK",
            "xg": "0.11",
            "price": "6.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Lucas Bergvall",
            "init": "LB",
            "xg": "0.11",
            "price": "5.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Pape Matar Sarr",
            "init": "PS",
            "xg": "0.10",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Archie Gray",
            "init": "AG",
            "xg": "0.09",
            "price": "4.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Conor Gallagher",
            "init": "CG",
            "xg": "0.09",
            "price": "5.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jo\u00e3o Maria Lobo Alves Palhares Costa Palhinha Gon\u00e7alves",
            "init": "JG",
            "xg": "0.07",
            "price": "5.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Cristian Romero",
            "init": "CR",
            "xg": "0.07",
            "price": "5.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Yves Bissouma",
            "init": "YB",
            "xg": "0.07",
            "price": "5.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Radu Dr\u0103gu\u0219in",
            "init": "RD",
            "xg": "0.05",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Djed Spence",
            "init": "DS",
            "xg": "0.04",
            "price": "4.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Pedro Porro Sauceda",
            "init": "PS",
            "xg": "0.03",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Rodrigo Bentancur",
            "init": "RB",
            "xg": "0.03",
            "price": "5.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Kevin Danso",
            "init": "KD",
            "xg": "0.02",
            "price": "4.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Destiny Udogie",
            "init": "DU",
            "xg": "0.02",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jo\u00e3o Victor de Souza Menezes",
            "init": "JM",
            "xg": "0.01",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Guglielmo Vicario",
            "init": "GV",
            "xg": "0.00",
            "price": "4.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Dane Scarlett",
            "init": "DS",
            "xg": "0.00",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Callum Olusesi",
            "init": "CO",
            "xg": "0.00",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jun'ai Byfield",
            "init": "JB",
            "xg": "0.00",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "James Rowswell",
            "init": "JR",
            "xg": "0.00",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        }
    ],
    "Wolves": [
        {
            "name": "Tom Edozie",
            "init": "TE",
            "xg": "2.55",
            "price": "4.3",
            "style": "tg-gold",
            "isSuper": false
        },
        {
            "name": "Tolu Arokodare",
            "init": "TA",
            "xg": "0.30",
            "price": "5.4",
            "style": "tg-silver",
            "isSuper": false
        },
        {
            "name": "Jhon Arias",
            "init": "JA",
            "xg": "0.27",
            "price": "4.9",
            "style": "tg-bronze",
            "isSuper": false
        },
        {
            "name": "Rodrigo Martins Gomes",
            "init": "RG",
            "xg": "0.26",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Hwang Hee-chan",
            "init": "HH",
            "xg": "0.17",
            "price": "5.6",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Marshall Munetsi",
            "init": "MM",
            "xg": "0.17",
            "price": "5.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Mateus Man\u00e9",
            "init": "MM",
            "xg": "0.10",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ladislav Krejc\u00ed",
            "init": "LK",
            "xg": "0.09",
            "price": "4.5",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Yerson Mosquera Valdelamar",
            "init": "YV",
            "xg": "0.09",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jean-Ricner Bellegarde",
            "init": "JB",
            "xg": "0.09",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Santiago Ignacio Bueno",
            "init": "SB",
            "xg": "0.08",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Fer L\u00f3pez Gonz\u00e1lez",
            "init": "FG",
            "xg": "0.06",
            "price": "5.1",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jo\u00e3o Victor Gomes da Silva",
            "init": "JS",
            "xg": "0.05",
            "price": "5.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Emmanuel Agbadou",
            "init": "EA",
            "xg": "0.05",
            "price": "4.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Adam Armstrong",
            "init": "AA",
            "xg": "0.03",
            "price": "5.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Andr\u00e9 Trindade da Costa Neto",
            "init": "AN",
            "xg": "0.02",
            "price": "5.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Hugo Bueno L\u00f3pez",
            "init": "HL",
            "xg": "0.02",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Toti Gomes",
            "init": "TG",
            "xg": "0.02",
            "price": "4.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Angel Gomes",
            "init": "AG",
            "xg": "0.02",
            "price": "4.7",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jackson Tchatchoua",
            "init": "JT",
            "xg": "0.01",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "David M\u00f8ller Wolfe",
            "init": "DW",
            "xg": "0.01",
            "price": "4.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Matt Doherty",
            "init": "MD",
            "xg": "0.01",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Jos\u00e9 Malheiro de S\u00e1",
            "init": "JS",
            "xg": "0.00",
            "price": "4.2",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Sam Johnstone",
            "init": "SJ",
            "xg": "0.00",
            "price": "4.4",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Ki-Jana Hoever",
            "init": "KH",
            "xg": "0.00",
            "price": "3.8",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Pedro Cardoso de Lima",
            "init": "PL",
            "xg": "0.00",
            "price": "4.0",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Tawanda Chirewa",
            "init": "TC",
            "xg": "0.00",
            "price": "4.3",
            "style": "tg-regular",
            "isSuper": false
        },
        {
            "name": "Sa\u0161a Kalajd\u017ei\u0107",
            "init": "SK",
            "xg": "0.00",
            "price": "4.9",
            "style": "tg-regular",
            "isSuper": false
        }
    ]
};
