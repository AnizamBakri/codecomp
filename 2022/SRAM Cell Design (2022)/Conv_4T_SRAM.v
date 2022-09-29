// DSCH 3.5

module sram4( WL,BLB,BL,Qbar,Q);
 input WL,BLB,BL;
 output Qbar,Q;
 wire ;
 pmos #(24) pmos_1(Qbar,vdd,Q); // 2.0u 0.12u
 nmos #(10) nmos_2(BL,Q,WL); // 1.0u 0.12u
 pmos #(24) pmos_3(Q,vdd,Qbar); // 2.0u 0.12u
 nmos #(24) nmos_4(Qbar,BLB,WL); // 1.0u 0.12u
endmodule

// Simulation parameters in Verilog Format
always
#2000 WL=~WL;
#1000 BLB=~BLB;
#1000 BL=~BL;

// Simulation parameters
// WL CLK 20 20
// BLB CLK 10 10
// BL CLK 10 10
