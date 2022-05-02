#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - function that check if the list is a palindrome
 * @head: the list to check
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
  int i = 0, j = 0, k;
  listint_t **tmp = head, **tmp2 = head;
  listint_t *tmpD1 = *tmp, *tmpD2 = *tmp2;
  listint_t *headD = *head;

  while (tmpD1->next->next)
  {
    tmpD1 = tmpD1->next;
    i++;
  }
  k = i / 2;
  if (i % 2 != 0)
    j--;
  for(; j < k + 1; j++)
  {
    tmpD1 = headD;
    for(i = k * 2; i - j != 0; i--)
    {
      tmpD1 = tmpD1->next;
    }
    if (tmpD1->next->n != tmpD2->n)
    {
      return (0);
    }
    tmpD2 = tmpD2->next;
  }
  return (1);
}
