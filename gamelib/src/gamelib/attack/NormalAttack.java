﻿package gamelib.attack;
public class NormalAttack extends Attack {
	public NormalAttack(int damage, int damageAmplifier) {
		super(damage, damage, damageAmplifier);
	}

	public NormalAttack() {
		super(0, 0, 100);
	}

	public int launch() {
		return getMaxDamage() * getDamageAmplifier() / 100;
	}
}