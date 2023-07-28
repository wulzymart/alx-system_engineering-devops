#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - loop for sleeping forever
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - entry point
 * Return: 0 success
 */
int main(void)
{
	pid_t child;
	int c = 5;

	while (c > 0)
	{
		child = fork();
		if (child != 0)
		{
			printf("Zombie process created, PID: %d\n", child);
			c--;
		}
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
