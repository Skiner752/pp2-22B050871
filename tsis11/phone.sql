--1 TASK

CREATE OR REPLACE FUNCTION get_contacts()
RETURNS TABLE ( name VARCHAR, surname VARCHAR, phone_number VARCHAR)
AS 
	$$
	BEGIN
  		RETURN QUERY 	
		select * from contacts;
	END; 
	$$ 
	LANGUAGE plpgsql;

SELECT * FROM get_contacts();

-- 2 TASK
CREATE OR REPLACE PROCEDURE ins_new(character varying , character varying , numeric)
AS
    $$
    BEGIN
        INSERT INTO contacts(name, surname, phone_number)
        VALUES ($1, $2, $3);
    END;
    $$ language plpgsql;

CALL ins_new('ruslan', 'vazovskiy' , 81234567894);
SELECT * FROM public.contacts

-- 3 TASK
CREATE OR REPLACE PROCEDURE arr_ins(VARIADIC list varchar[])
AS
$$
BEGIN
    FOR i in 1..array_upper(list, 1) by 2 LOOP
        IF list[i+1] ~ '8\d{4}' THEN
            INSERT INTO contacts (name,surname,phone_number) VALUES(list[i], '',list[i+1]);
        ELSE 
            RAISE NOTICE 'Your num % is incorrect', list[i+1];
        END IF;
    END LOOP;
END;
$$ 
LANGUAGE plpgsql;

CALL arr_ins('a' , '123435' , 'luntic' ,  '81234')


-- 4 TASK
CREATE OR REPLACE FUNCTION que(pg_size numeric , pg_number numeric)
RETURNS TABLE ( name VARCHAR, surname VARCHAR, phone_number VARCHAR)
AS 
	$$
	BEGIN
  		RETURN QUERY 	
		select * FROM contacts
        LIMIT pg_size OFFSET pg_number;
	END; 
	$$ 
	LANGUAGE plpgsql;


SELECT * FROM que(1 , 2);

-- 5 TASK
CREATE OR REPLACE PROCEDURE del(digits character varying)
AS
    $$
    BEGIN
        DELETE FROM contacts WHERE phone_number = digits;
    END;
    $$ LANGUAGE plpgsql;

CALL del('2');
SELECT * FROM public.contacts
