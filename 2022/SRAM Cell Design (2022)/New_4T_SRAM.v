// DSCH 3.5
// 21/6/2022 11:39:18 PM


module New4T( A,WordLine,QBar,Q);
 input A,WordLine;
 output QBar,Q;
 wire w6;
 nmos #(31) nmos_1(vss,Q,QBar); // 1.0u 0.12u
 nmos #(31) nmos_2(vss,QBar,Q); // 1.0u 0.12u
 nmos #(24) nmos_3(QBar,A,WordLine); // 1.0u 0.12u
 nmos #(24) nmos_4(Q,w6,WordLine); // 1.0u 0.12u
 nmos #(31) nmos_5(vss,w6,A); // 1.0u 0.12u
 pmos #(17) pmos_6(w6,vdd,A); // 2.0u 0.12u
endmodule

// Simulation parameters in Verilog Format
always
#1000 A=~A;
#2000 Word Line=~Word Line;

// Simulation parameters
// A CLK 10 10
// Word Line CLK 20 20
