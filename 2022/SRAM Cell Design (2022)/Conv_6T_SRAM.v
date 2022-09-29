// DSCH 3.5
// 21/6/2022 11:28:41 PM


module Conventional6T( BLB,BL,WL,Q,QBar);
 input BLB,BL,WL;
 output Q,QBar;
 wire ;
 nmos #(38) nmos_1(QBar,BLB,WL); // 1.0u 0.12u
 nmos #(38) nmos_2(Q,BL,WL); // 1.0u 0.12u
 nmos #(17) nmos_3(vss,QBar,Q); // 1.0u 0.12u
 pmos #(38) pmos_4(Q,vdd,QBar); // 2.0u 0.12u
 pmos #(38) pmos_5(QBar,vdd,Q); // 2.0u 0.12u
 nmos #(17) nmos_6(vss,Q,QBar); // 1.0u 0.12u
endmodule

// Simulation parameters in Verilog Format
always
#1000 BLB=~BLB;
#1000 BL=~BL;
#2000 WL=~WL;

// Simulation parameters
// BLB CLK 10 10
// BL CLK 10 10
// WL CLK 20 20
