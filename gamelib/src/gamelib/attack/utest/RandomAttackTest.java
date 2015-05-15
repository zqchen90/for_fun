package gamelib.attack.utest;

import gamelib.attack.*;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class RandomAttackTest {

  private RandomAttack emptyAttack;
  private RandomAttack attack1WithoutColdTime;
  private RandomAttack attack1;
  
  @Before
  public void setUp() throws Exception {
    emptyAttack = new RandomAttack();
    attack1WithoutColdTime = new RandomAttack(100, 50, 70, 100);
    attack1 = new RandomAttack(100, 50, 70, 100, 5);
  }
  
  @Test
  public void testLaunch() {
    int repeatTimes = 100;
    int repeat = 0;
    while (repeat < repeatTimes) {
      int damage = attack1.launch();
      if (damage > 0) {
        assertTrue(damage >= attack1.getMinDamage() * attack1.getDamageAmplifier());
        assertTrue(damage <= attack1.getMaxDamage() * attack1.getDamageAmplifier());
      }
      repeat++;
    }
  }

  @Test
  public void testRandomAttack() {
    assertEquals(0, emptyAttack.getMinDamage());
    assertEquals(0, emptyAttack.getMaxDamage());
    assertEquals(100, emptyAttack.getDamageAmplifier());
    assertEquals(100, emptyAttack.getProbability());
    assertEquals(0, emptyAttack.getColdTime());
  }

  @Test
  public void testRandomAttackIntIntIntIntInt() {
    assertEquals(50, attack1.getMinDamage());
    assertEquals(100, attack1.getMaxDamage());
    assertEquals(70, attack1.getProbability());
    assertEquals(100, attack1.getDamageAmplifier());
    assertEquals(5, attack1.getColdTime());
  }

  @Test
  public void testRandomAttackIntIntIntInt() {
    assertEquals(50, attack1WithoutColdTime.getMinDamage());
    assertEquals(100, attack1WithoutColdTime.getMaxDamage());
    assertEquals(70, attack1WithoutColdTime.getProbability());
    assertEquals(100, attack1WithoutColdTime.getDamageAmplifier());
    assertEquals(0, attack1WithoutColdTime.getColdTime());
  }

  @Test
  public void testSetColdTime() {
    assertEquals(5, attack1.getColdTime());
    attack1.setColdTime(10);
    assertEquals(10, attack1.getColdTime());
    
    assertEquals(0, attack1WithoutColdTime.getColdTime());
    attack1WithoutColdTime.setColdTime(10);
    assertEquals(10, attack1WithoutColdTime.getColdTime());
  }

  @Test
  public void testSetProbability() {
    assertEquals(70, attack1.getProbability());
    attack1.setProbability(80);
    assertEquals(80, attack1.getProbability());
  }
}
