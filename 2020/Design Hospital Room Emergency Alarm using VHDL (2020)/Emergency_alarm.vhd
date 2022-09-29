LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY alarm IS

PORT(i3, i2, i1, i0 : IN STD_LOGIC;
o1, o2, o3, o4, o5, o6, o7 : OUT STD_LOGIC);

END alarm;

ARCHITECTURE display OF alarm IS

SIGNAL input : STD_LOGIC_VECTOR (3 downto 0);
SIGNAL output : STD_LOGIC_VECTOR (6 downto 0);

BEGIN
input <= i3 & i2 & i1 & i0;

WITH input SELECT
output <=
"0000001" WHEN "0000",
"1001111" WHEN "0001",
"0010010" WHEN "0010",
"0000110" WHEN "0011",
"1001100" WHEN "0100",
"0100100" WHEN "0101",
"1100000" WHEN "0110",
"0001111" WHEN "0111",
"0000000" WHEN "1000",
"0001100" WHEN "1001",
"1111111" WHEN others;

o1 <= output(6);
o2 <= output(5);
o3 <= output(4);
o4 <= output(3);
o5 <= output(2);
o6 <= output(1);
o7 <= output(0);
END display;
