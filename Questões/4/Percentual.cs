using System;

class Program {
  static void Main(string[] args) {
    double sp = 67836.43;
    double rj = 36678.66;
    double mg = 29229.88;
    double es = 27165.48;
    double outros = 19849.53;
    double total = sp + rj + mg + es + outros;

    double spPerc = (sp / total) * 100;
    double rjPerc = (rj / total) * 100;
    double mgPerc = (mg / total) * 100;
    double esPerc = (es / total) * 100;
    double outrosPerc = (outros / total) * 100;

    Console.WriteLine("Percentual de representação de cada estado:");
    Console.WriteLine("SP: {0:F2}%", spPerc);
    Console.WriteLine("RJ: {0:F2}%", rjPerc);
    Console.WriteLine("MG: {0:F2}%", mgPerc);
    Console.WriteLine("ES: {0:F2}%", esPerc);
    Console.WriteLine("Outros: {0:F2}%", outrosPerc);
  }
}
