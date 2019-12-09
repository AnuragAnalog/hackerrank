create database if not exists hackerrank;
use hackerrank;

create table if not exists CITY
(
    ID int primary key,
    NAME varchar(30),
    COUNTRYCODE varchar(3),
    DISTRICT varchar(30),
    POPULATION int
);

insert into CITY values (4,"Mazar-e-Sharif","AFG","Balkh",127800);
insert into CITY values (11,"Groningen","NLD","Groningen",172701);
insert into CITY values (80,"Merlo","ARG","Buenos Aires",463846);
insert into CITY values (89,"San Isidro","ARG","Buenos Aires",306341);
insert into CITY values (91,"Malvinas Argentinas","ARG","Buenos Aires",290335);
insert into CITY values (124,"San Rafael","ARG","Mendoza",94651);
insert into CITY values (128,"Vanadzor","ARM","Lori",172700);
insert into CITY values (141,"Geelong","AUS","Victoria",125382);
insert into CITY values (142,"Townsville","AUS","Queensland",109914);
insert into CITY values (143,"Cairns","AUS","Queensland",92273);
insert into CITY values (146,"Sumqayit","AZE","Sumqayit",283000);
insert into CITY values (150,"Dhaka","BGD","Dhaka",3612850);
insert into CITY values (151,"Chittagong","BGD","Chittagong",1392860);
insert into CITY values (162,"Dinajpur","BGD","Rajshahi",127815);
insert into CITY values (166,"Tangail","BGD","Dhaka",106004);
insert into CITY values (168,"Pabna","BGD","Rajshahi",103277);
insert into CITY values (304,"Petrolina","BRA","Pernambuco",210540);
insert into CITY values (321,"Rio Grande","BRA","Rio Grande do Sul",182222);
insert into CITY values (379,"Palmas","BRA","Tocantins",121919);
insert into CITY values (431,"Angra dos Reis","BRA","Rio de Janeiro",96864);
insert into CITY values (473,"Stoke-on-Trent","GBR","England",252000);
insert into CITY values (478,"Aberdeen","GBR","Scotland",213070);
insert into CITY values (479,"Northampton","GBR","England",196000);
insert into CITY values (484,"Luton","GBR","England",183000);
insert into CITY values (510,"Slough","GBR","England",112000);
insert into CITY values (521,"Colchester","GBR","England",96063);
insert into CITY values (526,"Birkenhead","GBR","England",93087);
insert into CITY values (532,"Maidstone","GBR","England",90878);
insert into CITY values (540,"Plovdiv","BGR","Plovdiv",342584);
insert into CITY values (575,"Punta Arenas","CHL","Magallanes",125631);
insert into CITY values (628,"Qina","EGY","Qina",171275);
insert into CITY values (633,"Warraq al-Arab","EGY","Giza",127108);
insert into CITY values (657,"Zaragoza","ESP","Aragonia",603367);
insert into CITY values (665,"Vigo","ESP","Galicia",283670);
insert into CITY values (673,"Badalona","ESP","Katalonia",209635);
insert into CITY values (686,"Terrassa","ESP","Katalonia",168695);
insert into CITY values (720,"Kempton Park","ZAF","Gauteng",442633);
insert into CITY values (721,"Alberton","ZAF","Gauteng",410102);
insert into CITY values (732,"Klerksdorp","ZAF","North West",261911);
insert into CITY values (738,"Uitenhage","ZAF","Eastern Cape",192120);
insert into CITY values (743,"Brakpan","ZAF","Gauteng",171363);
insert into CITY values (784,"Iloilo","PHL","Western Visayas",365820);
insert into CITY values (789,"Iligan","PHL","Central Mindanao",285061);
insert into CITY values (805,"San Pablo","PHL","Southern Tagalog",207927);
insert into CITY values (811,"Binangonan","PHL","Southern Tagalog",187691);
insert into CITY values (820,"Legazpi","PHL","Bicol",157010);
insert into CITY values (858,"Hagonoy","PHL","Central Luzon",111425);
insert into CITY values (865,"San Jose","PHL","Central Luzon",108254);
insert into CITY values (886,"Bislig","PHL","Caraga",97860);
insert into CITY values (887,"Talavera","PHL","Central Luzon",97329);
insert into CITY values (892,"Capas","PHL","Central Luzon",95219);
insert into CITY values (902,"Libreville","GAB","Estuaire",419000);
insert into CITY values (906,"Kutaisi","GEO","Imereti",240900);
insert into CITY values (909,"Sohumi","GEO","Abhasia [Aphazeti]",111700);
insert into CITY values (931,"Delmas","HTI","Ouest",240429);
insert into CITY values (939,"Jakarta","IDN","Jakarta Raya",9604900);
insert into CITY values (941,"Bandung","IDN","West Java",2429000);
insert into CITY values (967,"Ciputat","IDN","West Java",270800);
insert into CITY values (981,"Karawang","IDN","West Java",145000);
insert into CITY values (997,"Cianjur","IDN","West Java",114300);
insert into CITY values (1002,"Citeureup","IDN","West Java",105100);
insert into CITY values (1004,"Klaten","IDN","Central Java",103300);
insert into CITY values (1021,"Sawangan","IDN","West Java",91100);
insert into CITY values (1032,"Nagpur","IND","Maharashtra",1624752);
insert into CITY values (1045,"Patna","IND","Bihar",917243);
insert into CITY values (1046,"Srinagar","IND","Jammu and Kashmir",892506);
insert into CITY values (1060,"Hubli-Dharwad","IND","Karnataka",648298);
insert into CITY values (1063,"Bareilly","IND","Uttar Pradesh",587211);
insert into CITY values (1092,"Bhilai","IND","Chhatisgarh",386159);
insert into CITY values (1099,"Jamnagar","IND","Gujarat",341637);
insert into CITY values (1119,"Davangere","IND","Karnataka",266082);
insert into CITY values (1122,"Bellary","IND","Karnataka",245391);
insert into CITY values (1126,"Muzaffarpur","IND","Bihar",241107);
insert into CITY values (1163,"Bally","IND","West Bengali",184474);
insert into CITY values (1164,"Bhilwara","IND","Rajasthan",183965);
insert into CITY values (1195,"Arrah (Ara)","IND","Bihar",157082);
insert into CITY values (1201,"Cuddalore","IND","Tamil Nadu",153086);
insert into CITY values (1203,"Dhanbad","IND","Jharkhand",151789);