import java.util

public class RandomAttack extends Attack {
  private int probability = 100;  // Max 100, min 0
  private int coldTime = 0;
  private int remainingColdTime = 0;
  private Random randomGenerator;
  private final int MAX_RANDOM_INT = 100;
  
  public Attack() {
    super(0, 0, 100);
    this.probability = 100;
    this.coldTime = 0;
    initialize();
  }

  public Attack(int maxDamage,
						 int minDamage,
						 int damageAmplifier,
						 int probability,
						 int coldTime) {
    super(maxDamage, minDamage, damageAmplifier);
    this.probability = probability;
    this.coldTime = coldTime;
    initialize();
  }

  private void initialize() {
    randomGenerator = new Random();
  }

  public int launch() {
    int damage = -1;  
    if (0 ==  remainingColdTime) {  // Not in cold time, can launch
      int randomNum = randomGenerator.nextInt(MAX_RANDOM_INT);
      if (randomNum < probability) {  // Launch successfully
        damage = minDamage +  randomNum * (maxDamage - minDamage) / probability;
      }
    }
    if (remainingColdTime > 0) {
      remainingColdTime -= 1;
    }
    if (damage > 0) {
      damage *= damageAmplifier;
    }
    return damage;
  }

}