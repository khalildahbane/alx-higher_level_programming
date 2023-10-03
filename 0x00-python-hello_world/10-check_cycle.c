<<<<<<< HEAD
#include "lists.h"



int check_cycle(listint_t *list)
{
	listint_t *hera, *tort;

	if (!list)
		return (0);

	while (hera && tort && tort->next)
	{
		hera = tort->next;
		tort = tort->next->next;
		if (hera == tort)
			return (1);
	}

	return (0);
}
=======

>>>>>>> refs/remotes/origin/master
