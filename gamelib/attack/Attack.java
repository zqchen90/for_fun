public abstract class Attack {
  private int maxDamage = 0;
  private int minDamage = 0;
  private int damageAmplifier = 100;  // is a precent number
  
  public Attack() {
    maxDamage = 0;
    minDamage = 0;
    damageAmplifier = 100;
  }

  public Attack(int maxDamage,
						 int minDamage,
						 int damageAmplifier,
    this.maxDamage = maxDamage;
    this.minDamage = minDamage;
    this.damageAmplifier = damageAmplifier;
  }

  public abstract int launch();

  public void setDamageAmplifier(int damageAmplifier) {
    this.damageAmplifier = damageAmplifier;
  }

}