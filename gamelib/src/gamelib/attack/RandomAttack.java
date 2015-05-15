package gamelib.attack;
import java.util.Random;

public class RandomAttack extends Attack {
  private int probability = 100;  // Max 100, Min 0
  private int coldTime = 0;
  private int remainingColdTime = 0;
  private Random randomGenerator;
  private final int MAX_RANDOM_INT = 100;
  
  
  public RandomAttack() {
    super(0, 0, 100);
    this.probability = 100;
    this.setColdTime(0);
    initialize();
  }

  
  public RandomAttack(int maxDamage,
						 int minDamage,
						 int probability,
             int damageAmplifier,
						 int coldTime) {
    super(maxDamage, minDamage, damageAmplifier);
    this.probability = probability;
    this.setColdTime(coldTime);
    initialize();
  }
 
  
  public RandomAttack(int maxDamage,
      int minDamage,
      int probability,
      int damageAmplifier) {
    super(maxDamage, minDamage, damageAmplifier);
    this.probability = probability;
    this.setColdTime(0);
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
        damage = getMinDamage() +  randomNum * (getMaxDamage() - getMinDamage()) / probability;
        remainingColdTime = getColdTime();
      }
    }
    // Modify remainingColdTime
    if (remainingColdTime > 0) {
      remainingColdTime -= 1;
    }
    if (damage > 0) {
      damage *= getDamageAmplifier();
    }
    return damage;
  }

  
  // Setters and Getters
  
  public int getColdTime() {
    return coldTime;
  }
  
  public void setColdTime(int coldTime) {
    this.coldTime = coldTime;
  }

  public void setProbability(int probability) {
    this.probability = probability;
  }
  
  public int getProbability() {
    return probability;
  }

}