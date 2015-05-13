public abstract class Attack {
  private int MaxDamage = 0;
  private int MinDamage = 0;
  private int Probability = 0;
  private int ColdTime = 0;
  
  public int getMaxDamage() {
    return MaxDamage;
  }
  public void setMaxDamage(int maxDamage) {
    MaxDamage = maxDamage;
  }
}