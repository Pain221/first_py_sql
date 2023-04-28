PGDMP         4    	            {         	   komunalka    15.2    15.2                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16398 	   komunalka    DATABASE     }   CREATE DATABASE komunalka WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE komunalka;
                postgres    false            �            1259    16411    accruals    TABLE       CREATE TABLE public.accruals (
    number_ls integer NOT NULL,
    accrual_date date NOT NULL,
    accrual_hvs numeric,
    accrual_gvs_heat_carrier numeric,
    accrual_gvs_thermal_energy numeric,
    accrual_total_gvs numeric,
    accrual_ee numeric,
    total_accrual numeric
);
    DROP TABLE public.accruals;
       public         heap    postgres    false            �            1259    16399 	   customers    TABLE       CREATE TABLE public.customers (
    number_ls integer NOT NULL,
    indications_date date NOT NULL,
    indications_hvs numeric,
    indications_gvs numeric,
    indications_ee_daytime numeric,
    number_of_residents integer,
    indications_ee_night numeric
);
    DROP TABLE public.customers;
       public         heap    postgres    false            �            1259    16428    users    TABLE     �   CREATE TABLE public.users (
    number_ls integer NOT NULL,
    password text NOT NULL,
    number_of_phone bigint NOT NULL,
    adress text NOT NULL
);
    DROP TABLE public.users;
       public         heap    postgres    false                      0    16411    accruals 
   TABLE DATA           �   COPY public.accruals (number_ls, accrual_date, accrual_hvs, accrual_gvs_heat_carrier, accrual_gvs_thermal_energy, accrual_total_gvs, accrual_ee, total_accrual) FROM stdin;
    public          postgres    false    215   �                  0    16399 	   customers 
   TABLE DATA           �   COPY public.customers (number_ls, indications_date, indications_hvs, indications_gvs, indications_ee_daytime, number_of_residents, indications_ee_night) FROM stdin;
    public          postgres    false    214   �                 0    16428    users 
   TABLE DATA           M   COPY public.users (number_ls, password, number_of_phone, adress) FROM stdin;
    public          postgres    false    216   �       o           2606    16417    accruals accruals_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.accruals
    ADD CONSTRAINT accruals_pkey PRIMARY KEY (number_ls, accrual_date);
 @   ALTER TABLE ONLY public.accruals DROP CONSTRAINT accruals_pkey;
       public            postgres    false    215    215            m           2606    16407    customers customers_pkey 
   CONSTRAINT     o   ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (number_ls, indications_date);
 B   ALTER TABLE ONLY public.customers DROP CONSTRAINT customers_pkey;
       public            postgres    false    214    214            q           2606    16434    users users_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (number_ls);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    216               �  x��X[��(�v���M�
z���p�۝d���scR�T!"[8��������������s�"�b�o��j�B�_���00�D���>BJ�t�	��\�uK��)�WY\)e�$��:�,��2nJ�2��j9W��QN>��YI���L�d��{l��/p7J�h�WM��M�ݩݸ���_��E�H�}!K��� �% "R�AW�Eq˞T��)�b�9����PV~Ѯ{� �o�I#�)��V���x�S#U������hc�¶�$_��b.��k�*���E��`�F�}æ��r?�K���;��t�b��3�c`�/A�|qlQ�'I�A��E+�-Q��A}�CAqev�5��'��ȵ�8�i���,)�h|NL�� B��F^Z�FuY�E����#����;Zʚ���_�G0yճ菻�fV;��̑Sb\9AM�����e� ɑ@L��X��䃱�����v+�+�I@�^�N^�/��s��$����Ʀ��7�ŋ�M<��ą�W�*���@��`�+��W�'�0ki��Q��F�F�nD����@�
�$9�x(hƏ��T�X\�2)�P�ݼ}#Q܊��j�1*�j�K$df�0AV����5��]^%�Q�Sr&�f����ޔ^��G�cBh��W.z&l�����RF�w�?��z��o�o�G�X0�O�#��V�T{��m2�8�������y~�\������{4�ǌ��fhw;OW�/Cr�Ip��B�y���¹�s�Ő��-�ېcR!��,TC������c�y�}�%�B�.}��ט�J���th����Å��4� 5trX�w<�S��<Y�eb�GE��ڝ�2��)����:�~�~&�S��t���UΕ��j���1��@� n+�Ǥ�����OE��Ћ:a��(��ȸ�"������x7EԶ�v�"K�S�1+�� ��7���n�}ZŲ�h���"|��;!m[�ƶ���Н��Yk�&28"J)�T�3=���p�%�v���z��=�����z����}�uHnү9�����E���ё�2L���8�������j~�PuE����7��~͋�S��:�G�����M�}2>���v�����          <  x��W[�� �6{驈�q����:5Q jLz�*����}YN?'�����<���?�G�ad�Ȁ�A
�YP �G�t����8I+���G�3H��xRޡ�$��e�0���`���%'k@f �"�Q�����D���1�ܘ��g���&�%��HR����<��b�'���R��}4�j��A�OB߻��AQ�
�]�f�#��i��(��s~F���=���B�����i�� p}Tx����o}_����p� ���݃���	�d���اs��Qt���	|Lq�Oq�P�h�?�y>/��'�8����#�q��|8��/��a�x�y_x���5�I�^�E�Ov{k"�#��p���n;�F?���.P��_�
Ͷ�<c;���pwr��<����p���X?p�s��t���V�F�����r�y6�H�,(�mAY�iB@�O+_������ދyZ�q�`�Lԗ���	��{�)Q�U@�n>�5�����,L�3�gK��Ҧ��t5��[83�HO��+���Io7�6I�%\��)�^VT���N���y��u�)-�����lq����S����æ�Mv���APn��E,n�n���1����rô+h�ʵR,<�]NZ{]��pi�n}_JH	A�Su�O�(��y���V��	�<BK���5���\��)zX.�iDR����A��B�>�.%U>K���T��z]�k��c)�K6����@�q�&��wɟ����b��ӊ�F3n���hm���-���n���n���_i�P��q����8� �6�         Y  x�}�Mn!�9Ŝ ��6p�V=A7]�Ԫ
����/	���|O��cCZ��^>�k�~~}_~�������<��5�r�u=_R�Ye�����r�Dd�ʔ9�v�����-\X4�l��e����� *FVX�2 V6����C������:�C�U^+��-�ֺr�-�?�z[L�qȱ��4���<��s��r�9��
������]`��	�D�h��&�a^%vb��*�81�EbC�	2��2Δ�I�I��N�N��:C�Ai
�����$�7�h<S��feaM����[��r�r��MR�M�B�$��7���R���&�     