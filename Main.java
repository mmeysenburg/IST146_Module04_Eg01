/* CheckingAccount Client, version 1
   Anderson, Franceschi
*/

public class Main {
  public static void main(String[] args) {
    BankAccount b1 = new BankAccount(1000);
    System.out.println("New bank account:\n" + b1);

    b1.deposit(1000);
    System.out.println("\nAfter depositing $1000:\n" + b1);

    b1.withdraw(500);
    System.out.println("\nAfter withdrawing $500:\n" + b1);

    CheckingAccount c5 = new CheckingAccount(100, 7.50);
    System.out.println("\n\nNew checking account:\n" + c5);

    c5.withdraw(95);
    System.out.println("\nAfter withdrawing $95:\n" + c5);

    System.out.println("\nApplying the monthly fee:");
    c5.applyMonthlyFee();
    if (c5.getBalance() < 0.0) {
      System.out.println("Warning: account is overdrawn!");
    }
    System.out.println(c5);
  }
}
