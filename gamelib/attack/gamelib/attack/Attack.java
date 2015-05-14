package gamelib.attack;
public abstract class Attack {
  protected int maxDamage = 0;
  protected int minDamage = 0;
  private int damageAmplifier = 100;  // is a percent number
  
  public Attack() {
    setMaxDamage(0);
    setMinDamage(0);
    setDamageAmplifier(100);
  }

  public Attack(int maxDamage,
						 int minDamage,
						 int damageAmplifier) {
    this.setMaxDamage(maxDamage);
    this.setMinDamage(minDamage);
    this.setDamageAmplifier(damageAmplifier);
  }

  public abstract int launch();

  // Setters and Getters
  
  public int getMinDamage() {
    return minDamage;
  }

  public void setMinDamage(int minDamage) {
    this.minDamage = minDamage;
  }

  public int getMaxDamage() {
    return maxDamage;
  }

  public void setMaxDamage(int maxDamage) {
    this.maxDamage = maxDamage;
  }

  public int getDamageAmplifier() {
    return damageAmplifier;
  }

  public void setDamageAmplifier(int damageAmplifier) {
    this.damageAmplifier = damageAmplifier;
  }

}