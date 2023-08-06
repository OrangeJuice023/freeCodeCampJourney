--
-- PostgreSQL database dump
--

-- Dumped from database version 12.9 (Ubuntu 12.9-2.pgdg20.04+1)
-- Dumped by pg_dump version 12.9 (Ubuntu 12.9-2.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE number_guess;
--
-- Name: number_guess; Type: DATABASE; Schema: -; Owner: freecodecamp
--

CREATE DATABASE number_guess WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C.UTF-8' LC_CTYPE = 'C.UTF-8';


ALTER DATABASE number_guess OWNER TO freecodecamp;

\connect number_guess

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: games; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.games (
    game_id integer NOT NULL,
    number_guesses integer NOT NULL,
    user_id integer
);


ALTER TABLE public.games OWNER TO freecodecamp;

--
-- Name: games_game_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.games_game_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.games_game_id_seq OWNER TO freecodecamp;

--
-- Name: games_game_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.games_game_id_seq OWNED BY public.games.game_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    username character varying(20) NOT NULL
);


ALTER TABLE public.users OWNER TO freecodecamp;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO freecodecamp;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: games game_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.games ALTER COLUMN game_id SET DEFAULT nextval('public.games_game_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: games; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.games VALUES (1, 635, 1);
INSERT INTO public.games VALUES (2, 14, 1);
INSERT INTO public.games VALUES (3, 76, 1);
INSERT INTO public.games VALUES (4, 785, 1);
INSERT INTO public.games VALUES (5, 519, 1);
INSERT INTO public.games VALUES (6, 276, 1);
INSERT INTO public.games VALUES (7, 965, 1);
INSERT INTO public.games VALUES (8, 788, 1);
INSERT INTO public.games VALUES (9, 795, 1);
INSERT INTO public.games VALUES (10, 738, 1);
INSERT INTO public.games VALUES (11, 887, 1);
INSERT INTO public.games VALUES (12, 738, 1);
INSERT INTO public.games VALUES (13, 144, 1);
INSERT INTO public.games VALUES (14, 650, 1);
INSERT INTO public.games VALUES (15, 367, 16);
INSERT INTO public.games VALUES (16, 910, 16);
INSERT INTO public.games VALUES (17, 191, 17);
INSERT INTO public.games VALUES (18, 230, 17);
INSERT INTO public.games VALUES (19, 774, 16);
INSERT INTO public.games VALUES (20, 819, 16);
INSERT INTO public.games VALUES (21, 139, 16);
INSERT INTO public.games VALUES (22, 930, 18);
INSERT INTO public.games VALUES (23, 413, 18);
INSERT INTO public.games VALUES (24, 551, 19);
INSERT INTO public.games VALUES (25, 319, 19);
INSERT INTO public.games VALUES (26, 720, 18);
INSERT INTO public.games VALUES (27, 297, 18);
INSERT INTO public.games VALUES (28, 711, 18);
INSERT INTO public.games VALUES (29, 164, 20);
INSERT INTO public.games VALUES (30, 625, 20);
INSERT INTO public.games VALUES (31, 226, 21);
INSERT INTO public.games VALUES (32, 392, 21);
INSERT INTO public.games VALUES (33, 852, 20);
INSERT INTO public.games VALUES (34, 706, 20);
INSERT INTO public.games VALUES (35, 359, 20);
INSERT INTO public.games VALUES (36, 161, 22);
INSERT INTO public.games VALUES (37, 117, 22);
INSERT INTO public.games VALUES (38, 146, 23);
INSERT INTO public.games VALUES (39, 115, 23);
INSERT INTO public.games VALUES (40, 300, 22);
INSERT INTO public.games VALUES (41, 651, 22);
INSERT INTO public.games VALUES (42, 105, 22);
INSERT INTO public.games VALUES (43, 8, 24);
INSERT INTO public.games VALUES (44, 191, 25);
INSERT INTO public.games VALUES (45, 403, 25);
INSERT INTO public.games VALUES (46, 63, 26);
INSERT INTO public.games VALUES (47, 124, 26);
INSERT INTO public.games VALUES (48, 662, 25);
INSERT INTO public.games VALUES (49, 81, 25);
INSERT INTO public.games VALUES (50, 198, 25);
INSERT INTO public.games VALUES (51, 449, 27);
INSERT INTO public.games VALUES (52, 499, 27);
INSERT INTO public.games VALUES (53, 980, 28);
INSERT INTO public.games VALUES (54, 658, 28);
INSERT INTO public.games VALUES (55, 48, 27);
INSERT INTO public.games VALUES (56, 807, 27);
INSERT INTO public.games VALUES (57, 927, 27);
INSERT INTO public.games VALUES (58, 413, 29);
INSERT INTO public.games VALUES (59, 346, 29);
INSERT INTO public.games VALUES (60, 717, 30);
INSERT INTO public.games VALUES (61, 405, 30);
INSERT INTO public.games VALUES (62, 510, 29);
INSERT INTO public.games VALUES (63, 722, 29);
INSERT INTO public.games VALUES (64, 584, 29);
INSERT INTO public.games VALUES (65, 116, 31);
INSERT INTO public.games VALUES (66, 495, 31);
INSERT INTO public.games VALUES (67, 243, 32);
INSERT INTO public.games VALUES (68, 837, 32);
INSERT INTO public.games VALUES (69, 506, 31);
INSERT INTO public.games VALUES (70, 581, 31);
INSERT INTO public.games VALUES (71, 413, 31);
INSERT INTO public.games VALUES (72, 22, 33);
INSERT INTO public.games VALUES (73, 523, 33);
INSERT INTO public.games VALUES (74, 872, 34);
INSERT INTO public.games VALUES (75, 847, 34);
INSERT INTO public.games VALUES (76, 488, 33);
INSERT INTO public.games VALUES (77, 30, 33);
INSERT INTO public.games VALUES (78, 705, 33);
INSERT INTO public.games VALUES (79, 364, 35);
INSERT INTO public.games VALUES (80, 437, 35);
INSERT INTO public.games VALUES (81, 991, 36);
INSERT INTO public.games VALUES (82, 267, 36);
INSERT INTO public.games VALUES (83, 561, 35);
INSERT INTO public.games VALUES (84, 673, 35);
INSERT INTO public.games VALUES (85, 974, 35);
INSERT INTO public.games VALUES (86, 343, 37);
INSERT INTO public.games VALUES (87, 328, 37);
INSERT INTO public.games VALUES (88, 335, 38);
INSERT INTO public.games VALUES (89, 191, 38);
INSERT INTO public.games VALUES (90, 75, 37);
INSERT INTO public.games VALUES (91, 493, 37);
INSERT INTO public.games VALUES (92, 330, 37);
INSERT INTO public.games VALUES (93, 136, 39);
INSERT INTO public.games VALUES (94, 538, 39);
INSERT INTO public.games VALUES (95, 537, 40);
INSERT INTO public.games VALUES (96, 395, 40);
INSERT INTO public.games VALUES (97, 413, 39);
INSERT INTO public.games VALUES (98, 213, 39);
INSERT INTO public.games VALUES (99, 194, 39);
INSERT INTO public.games VALUES (100, 821, 41);
INSERT INTO public.games VALUES (101, 555, 41);
INSERT INTO public.games VALUES (102, 383, 42);
INSERT INTO public.games VALUES (103, 994, 42);
INSERT INTO public.games VALUES (104, 423, 41);
INSERT INTO public.games VALUES (105, 345, 41);
INSERT INTO public.games VALUES (106, 451, 41);
INSERT INTO public.games VALUES (107, 240, 43);
INSERT INTO public.games VALUES (108, 238, 43);
INSERT INTO public.games VALUES (109, 489, 44);
INSERT INTO public.games VALUES (110, 753, 44);
INSERT INTO public.games VALUES (111, 324, 43);
INSERT INTO public.games VALUES (112, 181, 43);
INSERT INTO public.games VALUES (113, 570, 43);
INSERT INTO public.games VALUES (114, 456, 45);
INSERT INTO public.games VALUES (115, 647, 46);
INSERT INTO public.games VALUES (116, 537, 46);
INSERT INTO public.games VALUES (117, 598, 45);
INSERT INTO public.games VALUES (118, 626, 45);
INSERT INTO public.games VALUES (119, 754, 45);
INSERT INTO public.games VALUES (120, 926, 47);
INSERT INTO public.games VALUES (121, 402, 47);
INSERT INTO public.games VALUES (122, 183, 48);
INSERT INTO public.games VALUES (123, 5, 48);
INSERT INTO public.games VALUES (124, 636, 47);
INSERT INTO public.games VALUES (125, 66, 47);
INSERT INTO public.games VALUES (126, 615, 47);
INSERT INTO public.games VALUES (127, 517, 49);
INSERT INTO public.games VALUES (128, 332, 49);
INSERT INTO public.games VALUES (129, 639, 50);
INSERT INTO public.games VALUES (130, 675, 50);
INSERT INTO public.games VALUES (131, 10, 49);
INSERT INTO public.games VALUES (132, 522, 49);
INSERT INTO public.games VALUES (133, 980, 49);
INSERT INTO public.games VALUES (134, 404, 51);
INSERT INTO public.games VALUES (135, 360, 51);
INSERT INTO public.games VALUES (136, 408, 52);
INSERT INTO public.games VALUES (137, 591, 52);
INSERT INTO public.games VALUES (138, 97, 51);
INSERT INTO public.games VALUES (139, 445, 51);
INSERT INTO public.games VALUES (140, 33, 51);
INSERT INTO public.games VALUES (141, 192, 53);
INSERT INTO public.games VALUES (142, 890, 53);
INSERT INTO public.games VALUES (143, 939, 54);
INSERT INTO public.games VALUES (144, 416, 54);
INSERT INTO public.games VALUES (145, 1001, 53);
INSERT INTO public.games VALUES (146, 625, 53);
INSERT INTO public.games VALUES (147, 648, 53);
INSERT INTO public.games VALUES (148, 523, 63);
INSERT INTO public.games VALUES (149, 907, 63);
INSERT INTO public.games VALUES (150, 233, 64);
INSERT INTO public.games VALUES (151, 884, 64);
INSERT INTO public.games VALUES (152, 549, 63);
INSERT INTO public.games VALUES (153, 243, 63);
INSERT INTO public.games VALUES (154, 984, 63);
INSERT INTO public.games VALUES (155, 916, 65);
INSERT INTO public.games VALUES (156, 344, 65);
INSERT INTO public.games VALUES (157, 705, 66);
INSERT INTO public.games VALUES (158, 481, 66);
INSERT INTO public.games VALUES (159, 332, 65);
INSERT INTO public.games VALUES (160, 942, 65);
INSERT INTO public.games VALUES (161, 133, 65);
INSERT INTO public.games VALUES (162, 855, 67);
INSERT INTO public.games VALUES (163, 467, 67);
INSERT INTO public.games VALUES (164, 997, 68);
INSERT INTO public.games VALUES (165, 939, 68);
INSERT INTO public.games VALUES (166, 556, 67);
INSERT INTO public.games VALUES (167, 282, 67);
INSERT INTO public.games VALUES (168, 236, 67);
INSERT INTO public.games VALUES (169, 505, 69);
INSERT INTO public.games VALUES (170, 853, 69);
INSERT INTO public.games VALUES (171, 321, 70);
INSERT INTO public.games VALUES (172, 851, 70);
INSERT INTO public.games VALUES (173, 63, 69);
INSERT INTO public.games VALUES (174, 770, 69);
INSERT INTO public.games VALUES (175, 696, 69);
INSERT INTO public.games VALUES (176, 864, 71);
INSERT INTO public.games VALUES (177, 569, 71);
INSERT INTO public.games VALUES (178, 295, 72);
INSERT INTO public.games VALUES (179, 733, 72);
INSERT INTO public.games VALUES (180, 327, 71);
INSERT INTO public.games VALUES (181, 193, 71);
INSERT INTO public.games VALUES (182, 926, 71);
INSERT INTO public.games VALUES (183, 275, 73);
INSERT INTO public.games VALUES (184, 391, 73);
INSERT INTO public.games VALUES (185, 564, 74);
INSERT INTO public.games VALUES (186, 975, 74);
INSERT INTO public.games VALUES (187, 341, 73);
INSERT INTO public.games VALUES (188, 397, 73);
INSERT INTO public.games VALUES (189, 12, 73);
INSERT INTO public.games VALUES (190, 660, 75);
INSERT INTO public.games VALUES (191, 185, 75);
INSERT INTO public.games VALUES (192, 694, 76);
INSERT INTO public.games VALUES (193, 196, 76);
INSERT INTO public.games VALUES (194, 960, 75);
INSERT INTO public.games VALUES (195, 45, 75);
INSERT INTO public.games VALUES (196, 677, 75);
INSERT INTO public.games VALUES (197, 796, 77);
INSERT INTO public.games VALUES (198, 826, 77);
INSERT INTO public.games VALUES (199, 869, 78);
INSERT INTO public.games VALUES (200, 985, 78);
INSERT INTO public.games VALUES (201, 390, 77);
INSERT INTO public.games VALUES (202, 371, 77);
INSERT INTO public.games VALUES (203, 468, 77);
INSERT INTO public.games VALUES (204, 921, 79);
INSERT INTO public.games VALUES (205, 539, 79);
INSERT INTO public.games VALUES (206, 858, 80);
INSERT INTO public.games VALUES (207, 500, 80);
INSERT INTO public.games VALUES (208, 979, 79);
INSERT INTO public.games VALUES (209, 539, 79);
INSERT INTO public.games VALUES (210, 628, 79);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.users VALUES (1, '');
INSERT INTO public.users VALUES (16, 'user_1691340212421');
INSERT INTO public.users VALUES (17, 'user_1691340212420');
INSERT INTO public.users VALUES (18, 'user_1691340364614');
INSERT INTO public.users VALUES (19, 'user_1691340364613');
INSERT INTO public.users VALUES (20, 'user_1691340453455');
INSERT INTO public.users VALUES (21, 'user_1691340453454');
INSERT INTO public.users VALUES (22, 'user_1691340528113');
INSERT INTO public.users VALUES (23, 'user_1691340528112');
INSERT INTO public.users VALUES (24, 'Hello');
INSERT INTO public.users VALUES (25, 'user_1691340627446');
INSERT INTO public.users VALUES (26, 'user_1691340627445');
INSERT INTO public.users VALUES (27, 'user_1691340712643');
INSERT INTO public.users VALUES (28, 'user_1691340712642');
INSERT INTO public.users VALUES (29, 'user_1691340720761');
INSERT INTO public.users VALUES (30, 'user_1691340720760');
INSERT INTO public.users VALUES (31, 'user_1691340759038');
INSERT INTO public.users VALUES (32, 'user_1691340759037');
INSERT INTO public.users VALUES (33, 'user_1691340781648');
INSERT INTO public.users VALUES (34, 'user_1691340781647');
INSERT INTO public.users VALUES (35, 'user_1691340837077');
INSERT INTO public.users VALUES (36, 'user_1691340837076');
INSERT INTO public.users VALUES (37, 'user_1691340858534');
INSERT INTO public.users VALUES (38, 'user_1691340858533');
INSERT INTO public.users VALUES (39, 'user_1691340905708');
INSERT INTO public.users VALUES (40, 'user_1691340905707');
INSERT INTO public.users VALUES (41, 'user_1691340945159');
INSERT INTO public.users VALUES (42, 'user_1691340945158');
INSERT INTO public.users VALUES (43, 'user_1691340986462');
INSERT INTO public.users VALUES (44, 'user_1691340986461');
INSERT INTO public.users VALUES (45, 'user_1691341064994');
INSERT INTO public.users VALUES (46, 'user_1691341064993');
INSERT INTO public.users VALUES (47, 'user_1691341074741');
INSERT INTO public.users VALUES (48, 'user_1691341074740');
INSERT INTO public.users VALUES (49, 'user_1691341082913');
INSERT INTO public.users VALUES (50, 'user_1691341082912');
INSERT INTO public.users VALUES (51, 'user_1691341231789');
INSERT INTO public.users VALUES (52, 'user_1691341231788');
INSERT INTO public.users VALUES (53, 'user_1691341267658');
INSERT INTO public.users VALUES (54, 'user_1691341267657');
INSERT INTO public.users VALUES (55, 'user_1691341319577');
INSERT INTO public.users VALUES (56, 'user_1691341319576');
INSERT INTO public.users VALUES (57, 'user_1691341331164');
INSERT INTO public.users VALUES (58, 'user_1691341331163');
INSERT INTO public.users VALUES (59, 'user_1691341338406');
INSERT INTO public.users VALUES (60, 'user_1691341338405');
INSERT INTO public.users VALUES (61, 'user_1691341398832');
INSERT INTO public.users VALUES (62, 'user_1691341398831');
INSERT INTO public.users VALUES (63, 'user_1691341411612');
INSERT INTO public.users VALUES (64, 'user_1691341411611');
INSERT INTO public.users VALUES (65, 'user_1691341424645');
INSERT INTO public.users VALUES (66, 'user_1691341424644');
INSERT INTO public.users VALUES (67, 'user_1691341515842');
INSERT INTO public.users VALUES (68, 'user_1691341515841');
INSERT INTO public.users VALUES (69, 'user_1691341532060');
INSERT INTO public.users VALUES (70, 'user_1691341532059');
INSERT INTO public.users VALUES (71, 'user_1691341541846');
INSERT INTO public.users VALUES (72, 'user_1691341541845');
INSERT INTO public.users VALUES (73, 'user_1691341782910');
INSERT INTO public.users VALUES (74, 'user_1691341782909');
INSERT INTO public.users VALUES (75, 'user_1691341789177');
INSERT INTO public.users VALUES (76, 'user_1691341789176');
INSERT INTO public.users VALUES (77, 'user_1691341860643');
INSERT INTO public.users VALUES (78, 'user_1691341860642');
INSERT INTO public.users VALUES (79, 'user_1691341924224');
INSERT INTO public.users VALUES (80, 'user_1691341924223');


--
-- Name: games_game_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.games_game_id_seq', 210, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.users_user_id_seq', 80, true);


--
-- Name: games games_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.games
    ADD CONSTRAINT games_pkey PRIMARY KEY (game_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: games games_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.games
    ADD CONSTRAINT games_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

